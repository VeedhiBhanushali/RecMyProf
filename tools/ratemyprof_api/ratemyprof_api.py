import requests
import json
import math
import csv
import os

from .professor import Professor
# This code has been tested using Python 3.6 interpreter and Linux (Ubuntu).
# It should run under Windows, if anything you may need to make some adjustments for the file paths of the CSV files.


class ProfessorNotFound(Exception):
    def __init__(self, search_argument, search_parameter: str = "Name"):

        # What the client is looking for. Ex: "Professor Pattis"
        self.search_argument = self.search_argument

        # The search criteria. Ex: Last Name
        self.search_parameter = search_parameter

    def __str__(self):

        return (
            f"Proessor not found"
            + f" The search argument {self.search_argument} did not"
            + f" match with any professor's {self.search_parameter}"
        )


class RateMyProfApi:
    def __init__(self, school_id: str = "1074", testing: bool = False):
        self.UniversityId = school_id
        self.base_url = "https://www.ratemyprofessors.com/filter/professor/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        if not os.path.exists("SchoolID_" + str(self.UniversityId)):
            os.mkdir("SchoolID_" + str(self.UniversityId))

        # dict of Professor
        self.professors = self.scrape_professors(testing)
        self.indexnumber = False

    def _make_request(self, url: str) -> dict:
        """Make a request with error handling"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Some RMP responses include a BOM character, remove it
            content = response.content.decode('utf-8-sig')
            return json.loads(content)
        except Exception as e:
            print(f"Request failed for URL {url}: {e}")
            return {}

    def get_num_of_professors(self, school_id: str) -> int:
        """Get the total number of professors for a school"""
        url = f"{self.base_url}?page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid={school_id}"
        data = self._make_request(url)
        if not data:
            return 0
        return data.get("remaining", 0) + len(data.get("professors", []))

    def scrape_professors(self, testing: bool = False) -> dict:
        """Scrape professor data from RMP"""
        professors = {}
        num_of_prof = self.get_num_of_professors(self.UniversityId)
        if num_of_prof == 0:
            return professors

        num_of_pages = math.ceil(num_of_prof / 20)
        for i in range(1, num_of_pages + 1):
            url = f"{self.base_url}?page={i}&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid={self.UniversityId}"
            data = self._make_request(url)
            
            if not data or "professors" not in data:
                continue

            for prof_data in data["professors"]:
                try:
                    professor = Professor(
                        prof_data.get("tid", 0),
                        prof_data.get("tFname", ""),
                        prof_data.get("tLname", ""),
                        int(prof_data.get("tNumRatings", 0)),
                        prof_data.get("overall_rating", "N/A")
                    )
                    # Add additional professor data
                    professor.department = prof_data.get("tDept", "Not specified")
                    professor.would_take_again = prof_data.get("would_take_again_percent", "N/A")
                    professor.difficulty = prof_data.get("difficulty", "N/A")
                    
                    print(f"Found professor: {professor.first_name} {professor.last_name} in {professor.department}")
                    professors[professor.ratemyprof_id] = professor
                except Exception as e:
                    print(f"Error processing professor data: {e}")
                    print(f"Raw professor data: {prof_data}")

            if testing and i > 1:
                break

        return professors

    def search_professor(self, ProfessorName):
        self.indexnumber = self.get_professor_index(ProfessorName)
        self.print_professor_info()
        return self.indexnumber



    def get_professor_by_last_name(
        self, last_name
    ) -> Professor:
        '''
        Return the first professor with the matching last name.
        Case insenstive.
        '''
        last_name = last_name.lower()
        for name in professors:
            if last_name == professors[name].last_name.lower():
                return professors[name]

        # Raise error if no matching professor found
        raise ProfessorNotFound(last_name, "Last Name")





    def WriteProfessorListToCSV(self):
        csv_columns = [
            "tDept",
            "tSid",
            "institution_name",
            "tFname",
            "tMiddlename",
            "tLname",
            "tid",
            "tNumRatings",
            "rating_class",
            "contentType",
            "categoryType",
            "overall_rating",
        ]
        csv_file = "SchoolID_" + str(self.UniversityId) + ".csv"
        with open(csv_file, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in self.professorlist:
                writer.writerow(data)

    def create_reviews_list(self, tid):
        tempreviewslist = []
        num_of_reviews = self.get_num_of_reviews(tid)
        # RMP only loads 20 reviews per page,
        # so num_of_pages tells us how many pages we need to get all the reviews
        num_of_pages = math.ceil(num_of_reviews / 20)
        i = 1
        while i <= num_of_pages:
            page = requests.get(
                "https://www.ratemyprofessors.com/paginate/professors/ratings?tid="
                + str(tid)
                + "&filter=&courseCode=&page="
                + str(i)
            )
            temp_jsonpage = json.loads(page.content)
            temp_list = temp_jsonpage["ratings"]
            tempreviewslist.extend(temp_list)
            i += 1
        return tempreviewslist

    def get_num_of_reviews(self, id):
        page = requests.get(
            "https://www.ratemyprofessors.com/paginate/professors/ratings?tid="
            + str(id)
            + "&filter=&courseCode=&page=1"
        )
        temp_jsonpage = json.loads(page.content)
        num_of_reviews = temp_jsonpage["remaining"] + 20
        return num_of_reviews

    def WriteReviewsListToCSV(self, rlist, tid):
        csv_columns = [
            "attendance",
            "clarityColor",
            "easyColor",
            "helpColor",
            "helpCount",
            "id",
            "notHelpCount",
            "onlineClass",
            "quality",
            "rClarity",
            "rClass",
            "rComments",
            "rDate",
            "rEasy",
            "rEasyString",
            "rErrorMsg",
            "rHelpful",
            "rInterest",
            "rOverall",
            "rOverallString",
            "rStatus",
            "rTextBookUse",
            "rTimestamp",
            "rWouldTakeAgain",
            "sId",
            "takenForCredit",
            "teacher",
            "teacherGrade",
            "teacherRatingTags",
            "unUsefulGrouping",
            "usefulGrouping",
        ]
        csv_file = (
            "./SchoolID_" + str(self.UniversityId) + "/TeacherID_" + str(tid) + ".csv"
        )
        with open(csv_file, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in rlist:
                writer.writerow(data)


# Time for some examples!
if __name__ == '__main__':

    # Getting general professor info!
    uci = RateMyProfApi(1074)


    # uci.search_professor("Pattis")
    # uci.print_professor_detail("overall_rating")
    '''
    MassInstTech = RateMyProfApi(580)
    MassInstTech.search_professor("Robert Berwick")
    MassInstTech.print_professor_detail("overall_rating")

    # Let's try the above class out to get data from a number of schools!
    # William Patterson, Case Western, University of Chicago, CMU, Princeton, Yale, MIT, UTexas at Austin, Duke, Stanford, Rice, Tufts
    # For simple test, try tid 97904 at school 1205
    schools = [1205, 186, 1085, 181, 780, 1222, 580, 1255, 1350, 953, 799, 1040]
    for school in schools:
        print("=== Processing School " + str(school) + " ===")
        rmps = RateMyProfApi(school)
        rmps.WriteProfessorListToCSV()
        professors = rmps.get_professor_list()
        for professor in professors:
            reviewslist = rmps.create_reviews_list(professor.get("tid"))
            rmps.WriteReviewsListToCSV(reviewslist, professor.get("tid"))

    '''
