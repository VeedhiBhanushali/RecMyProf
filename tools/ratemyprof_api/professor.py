class Professor:
    def __init__(self, ratemyprof_id: int, first_name: str, last_name: str, num_of_ratings: int, overall_rating):
        self.ratemyprof_id = ratemyprof_id
        self.name = f"{first_name} {last_name}"
        self.first_name = first_name
        self.last_name = last_name
        self.num_ratings = num_of_ratings
        self.department = "Not specified"
        self.would_take_again = "N/A"
        self.difficulty = "N/A"

        if self.num_ratings < 1 or overall_rating == "N/A":
            self.overall_rating = "N/A"
        else:
            try:
                self.overall_rating = float(overall_rating)
            except:
                self.overall_rating = "N/A"
