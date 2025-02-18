"""
SJSU Professor Database and Search Functionality
"""

# This will store the SJSU professor database
SJSU_PROFESSORS = {
    "abera_jiru": {
        "first_name": "Abera",
        "last_name": "Jiru",
        "department": "Mathematics",
        "overall_rating": 2.7,
        "quality": 2.7,
        "num_ratings": 90,
        "would_take_again": 50.0,
        "difficulty": 3.1
    },
    "ahmad_yazdankhah": {
        "first_name": "Ahmad",
        "last_name": "Yazdankhah",
        "department": "Computer Science",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 95,
        "would_take_again": 72.0,
        "difficulty": 3.1,
        "contact": {
            "email": "ahmad.yazdankhah@sjsu.edu",
            "office": "MQH 412",
            "office_hours": "Mon/Wed 1:30-2:30pm",
            "phone": "(408) 924-5083"
        },
        "academic": {
            "title": "Lecturer",
            "research_interests": ["Software Engineering", "Programming Languages"],
            "current_courses": ["CS46B", "CS151", "CS166"]
        },
    },
    "faranak_abri": {
        "first_name": "Faranak",
        "last_name": "Abri",
        "department": "Computer Science",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 23,
        "would_take_again": 79.0,
        "difficulty": 2.8,
        "tags": [
            "EXTRA CREDIT",
            "LOTS OF HOMEWORK",
            "ACCESSIBLE OUTSIDE CLASS",
            "AMAZING LECTURES",
            "CARING"
        ],
        "rating_distribution": {
            "5": 9,
            "4": 8,
            "3": 2,
            "2": 3,
            "1": 1
        },
        "courses": ["CS46B", "CS286"],
        "teaching_style": [
            "Uses Zybooks for homework",
            "Two midterms (20% each)",
            "Final exam (25%)",
            "Generous extra credit (5-10%)",
            "Optional attendance",
            "Lab component on Fridays",
            "Multiple choice and coding exams",
            "Lenient with extensions"
        ],
        "notes": [
            "Accent can be difficult to understand",
            "No practice exams provided",
            "Heavy reliance on Zybooks",
            "Tests based on in-class activities",
            "Strong in Machine Learning/NLP topics"
        ],
        "contact": {
            "email": "faranak.abri@sjsu.edu",
            "office": "MQH 232",
            "office_hours": "Mon/Wed 3:00-4:00pm",
            "zoom_link": "https://sjsu.zoom.us/j/...",
            "phone": "(408) 924-5134"
        },
        "academic": {
            "title": "Assistant Professor",
            "research_interests": [
                "Machine Learning",
                "Natural Language Processing",
                "Data Mining"
            ],
            "current_courses": ["CS46B", "CS156", "CS256"]
        },
    },
    "william_andreopoulos": {
        "first_name": "William",
        "last_name": "Andreopoulos",
        "department": "Computer Science",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 35,
        "would_take_again": 80.0,
        "difficulty": 3.2,
        "contact": {
            "email": "william.andreopoulos@sjsu.edu",
            "office": "MQH 414",
            "office_hours": "Tue/Thu 4:30-5:30pm",
            "phone": "(408) 924-5161",
            "website": "https://www.cs.sjsu.edu/~andreopoulos/"
        },
        "academic": {
            "title": "Associate Professor",
            "research_interests": ["Bioinformatics", "Data Mining", "Machine Learning"],
            "current_courses": ["CS122", "CS155", "CS255"]
        },
    },
    "thomas_austin": {
        "first_name": "Thomas",
        "last_name": "Austin",
        "department": "Computer Science",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 16,
        "would_take_again": 100.0,
        "difficulty": 3.6,
        "contact": {
            "email": "thomas.austin@sjsu.edu",
            "office": "MQH 413",
            "office_hours": "Tue/Thu 10:30-11:30am",
            "phone": "(408) 924-5147",
            "website": "https://www.cs.sjsu.edu/~austin/"
        },
        "academic": {
            "title": "Associate Professor",
            "research_interests": ["Programming Languages", "Security", "Software Engineering"],
            "current_courses": ["CS152", "CS160", "CS166"]
        },
    },
    "ali_arsanjani": {
        "first_name": "Ali",
        "last_name": "Arsanjani",
        "department": "Computer Science",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 60,
        "would_take_again": 95.0,
        "difficulty": 3.7,
        "contact": {
            "email": "ali.arsanjani@sjsu.edu",
            "office": "MQH 231",
            "office_hours": "Mon/Wed 5:45-6:45pm",
            "phone": "(408) 924-5087"
        },
        "academic": {
            "title": "Assistant Professor",
            "research_interests": ["Cloud Computing", "Software Architecture", "AI"],
            "current_courses": ["CS160", "CS172", "CS272"]
        },
    },
    "tahereh_arabghalizi": {
        "first_name": "Tahereh",
        "last_name": "Arabghalizi",
        "department": "Computer Science",
        "overall_rating": 1.8,
        "quality": 1.8,
        "num_ratings": 34,
        "would_take_again": 21.0,
        "difficulty": 4.1,
        "contact": {
            "email": "tahereh.arabghalizi@sjsu.edu",
            "office": "MQH 228",
            "office_hours": "Mon/Wed 4:30-5:30pm",
            "phone": "(408) 924-5108"
        },
        "academic": {
            "title": "Assistant Professor",
            "research_interests": ["Computer Networks", "Network Security", "IoT"],
            "current_courses": ["CS158A", "CS166", "CS265"]
        },
    },
    "alexandra_chakarov": {
        "first_name": "Alexandra",
        "last_name": "Chakarov",
        "department": "Computer Science",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 19,
        "would_take_again": 79.0,
        "difficulty": 3.0,
        "contact": {
            "email": "alexandra.chakarov@sjsu.edu",
            "office": "MQH 233",
            "office_hours": "Tue/Thu 12:00-1:00pm",
            "phone": "(408) 924-5122"
        },
        "academic": {
            "title": "Assistant Professor",
            "research_interests": ["Software Engineering", "Program Analysis", "CS Education"],
            "current_courses": ["CS46B", "CS152", "CS252"]
        },
    },
    "david_anastasiu": {
        "first_name": "David",
        "last_name": "Anastasiu",
        "department": "Computer Engineering",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 13,
        "would_take_again": 85.0,
        "difficulty": 3.9,
        "contact": {
            "email": "david.anastasiu@sjsu.edu",
            "office": "ENG 281",
            "office_hours": "Mon/Wed 3:00-4:00pm, Thu 10:00-11:00am",
            "phone": "(408) 924-3489",
            "website": "https://www.sjsu.edu/people/david.anastasiu/"
        },
        "academic": {
            "title": "Associate Professor",
            "research_interests": ["Data Mining", "Machine Learning", "High Performance Computing"],
            "current_courses": ["CS156", "CS256", "CS267"]
        },
    },
    "aikaterini_potika": {
        "first_name": "Aikaterini",
        "last_name": "Potika",
        "department": "Computer Engineering",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 19,
        "would_take_again": 34.0,
        "difficulty": 2.4,
        "contact": {
            "email": "aikaterini.potika@sjsu.edu",
            "office": "ENG 283",
            "office_hours": "Mon/Wed 1:30-2:30pm",
            "phone": "(408) 924-3204",
            "website": "https://www.sjsu.edu/people/aikaterini.potika"
        },
        "academic": {
            "title": "Associate Professor",
            "research_interests": ["Graph Theory", "Social Networks", "Data Mining"],
            "current_courses": ["CS146", "CS255", "CS257"]
        },
    },
    "ron_mak": {
        "first_name": "Ron",
        "last_name": "Mak",
        "department": "Computer Engineering",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 26,
        "would_take_again": 91.0,
        "difficulty": 3.3,
        "contact": {
            "email": "ron.mak@sjsu.edu",
            "office": "ENG 250",
            "office_hours": "Tue/Thu 3:00-4:00pm",
            "phone": "(408) 924-5167",
            "website": "https://www.cs.sjsu.edu/~mak/"
        },
        "academic": {
            "title": "Professor",
            "research_interests": ["Software Engineering", "Programming Languages", "Compiler Design"],
            "current_courses": ["CS153", "CS249", "CS252"]
        },
    },
    "ahmet_bindal": {
        "first_name": "Ahmet",
        "last_name": "Bindal",
        "department": "Computer Engineering",
        "overall_rating": 3.4,
        "quality": 3.4,
        "num_ratings": 52,
        "would_take_again": 50.0,
        "difficulty": 3.7
    },
    "andrew_bond": {
        "first_name": "Andrew",
        "last_name": "Bond",
        "department": "Computer Engineering",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 31,
        "would_take_again": 45.0,
        "difficulty": 2.8
    },
    "spoorthy_ananthaiah": {
        "first_name": "Spoorthy",
        "last_name": "Ananthaiah",
        "department": "Computer Engineering",
        "overall_rating": 2.8,
        "quality": 2.8,
        "num_ratings": 8,
        "would_take_again": 60.0,
        "difficulty": 3.4
    },
    "albert_chang": {
        "first_name": "Albert",
        "last_name": "Chang",
        "department": "Mathematics",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 24,
        "would_take_again": 67.0,
        "difficulty": 2.3
    },
    "andrea_gottlieb": {
        "first_name": "Andrea",
        "last_name": "Gottlieb",
        "department": "Mathematics",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 43,
        "would_take_again": 64.0,
        "difficulty": 2.8
    },
    "angela_tran": {
        "first_name": "Angela",
        "last_name": "Tran",
        "department": "Mathematics",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 34,
        "would_take_again": 48.0,
        "difficulty": 2.7
    },
    "roger_alperin": {
        "first_name": "Roger",
        "last_name": "Alperin",
        "department": "Mathematics",
        "overall_rating": 3.2,
        "quality": 3.2,
        "num_ratings": 42,
        "would_take_again": 0.0,
        "difficulty": 2.9
    },
    "andrew_jianyu_yu": {
        "first_name": "Andrew Jianyu",
        "last_name": "Yu",
        "department": "Mathematics",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 40,
        "would_take_again": 0.0,
        "difficulty": 1.5
    },
    "anh_nguyen": {
        "first_name": "Anh",
        "last_name": "Nguyen",
        "department": "Mathematics",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 50,
        "would_take_again": 85.0,
        "difficulty": 1.7
    },
    "anna_strong": {
        "first_name": "Anna",
        "last_name": "Strong",
        "department": "Mathematics",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 76,
        "would_take_again": 75.0,
        "difficulty": 2.5
    },
    "alana_bailey": {
        "first_name": "Alana",
        "last_name": "Bailey",
        "department": "Mathematics",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 14,
        "would_take_again": 100.0,
        "difficulty": 1.9
    },
    "anastasiya_pryvarnikova": {
        "first_name": "Anastasiya",
        "last_name": "Pryvarnikova",
        "department": "Mathematics",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 34,
        "would_take_again": 84.0,
        "difficulty": 2.2
    },
    "abbas_moallem": {
        "first_name": "Abbas",
        "last_name": "Moallem",
        "department": "Industrial Engineering",
        "overall_rating": 1.9,
        "quality": 1.9,
        "num_ratings": 39,
        "would_take_again": 24.0,
        "difficulty": 3.6
    },
    "ammar_rayes": {
        "first_name": "Ammar",
        "last_name": "Rayes",
        "department": "Industrial Engineering",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 19,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "ayca_erdogan": {
        "first_name": "Ayca",
        "last_name": "Erdogan",
        "department": "Industrial Engineering",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 22,
        "would_take_again": 69.0,
        "difficulty": 3.6
    },
    "supreeta_amin": {
        "first_name": "Supreeta",
        "last_name": "Amin",
        "department": "Industrial Engineering",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 15,
        "would_take_again": 67.0,
        "difficulty": 3.2
    },
    "anil_kumar": {
        "first_name": "Anil",
        "last_name": "Kumar",
        "department": "Industrial Engineering",
        "overall_rating": 2.1,
        "quality": 2.1,
        "num_ratings": 14,
        "would_take_again": 22.0,
        "difficulty": 4.4
    },
    "mithal_albassam": {
        "first_name": "Mithal",
        "last_name": "Albassam",
        "department": "Industrial Engineering",
        "overall_rating": 1.6,
        "quality": 1.6,
        "num_ratings": 7,
        "would_take_again": 0.0,
        "difficulty": 4.4
    },
    "tony_andre": {
        "first_name": "Tony",
        "last_name": "Andre",
        "department": "Industrial Engineering",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 3,
        "would_take_again": 50.0,
        "difficulty": 3.7
    },
    "albert_schendan": {
        "first_name": "Albert",
        "last_name": "Schendan",
        "department": "Political Science",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 161,
        "would_take_again": 39.0,
        "difficulty": 3.4
    },
    "albert_wong": {
        "first_name": "Albert",
        "last_name": "Wong",
        "department": "Civil Engineering",
        "overall_rating": 2.5,
        "quality": 2.5,
        "num_ratings": 39,
        "would_take_again": 43.0,
        "difficulty": 4.0
    },
    "thalia_anagnos": {
        "first_name": "Thalia",
        "last_name": "Anagnos",
        "department": "Civil Engineering",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 23,
        "would_take_again": 0.0,
        "difficulty": 2.4
    },
    "akthem_al_manaseer": {
        "first_name": "Akthem",
        "last_name": "Al-Manaseer",
        "department": "Civil Engineering",
        "overall_rating": 2.7,
        "quality": 2.7,
        "num_ratings": 78,
        "would_take_again": 100.0,
        "difficulty": 3.7
    },
    "ajay_singhal": {
        "first_name": "Ajay",
        "last_name": "Singhal",
        "department": "Civil Engineering",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 25,
        "would_take_again": 100.0,
        "difficulty": 3.7
    },
    "amin_ghafooripour": {
        "first_name": "Amin",
        "last_name": "Ghafooripour",
        "department": "Civil Engineering",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 13,
        "would_take_again": 93.0,
        "difficulty": 2.2
    },
    "anne_marie_moore": {
        "first_name": "Anne-Marie",
        "last_name": "Moore",
        "department": "Civil Engineering",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 3,
        "would_take_again": 34.0,
        "difficulty": 4.3
    },
    "ashkan_agharahmanian": {
        "first_name": "Ashkan",
        "last_name": "Agharahmanian",
        "department": "Civil Engineering",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "ali_oskoorouchi": {
        "first_name": "Ali",
        "last_name": "Oskoorouchi",
        "department": "Civil Engineering",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 8,
        "would_take_again": 0.0,
        "difficulty": 3.6
    },
    "amir_armani": {
        "first_name": "Amir",
        "last_name": "Armani",
        "department": "Mechanical Engineering",
        "overall_rating": 1.8,
        "quality": 1.8,
        "num_ratings": 9,
        "would_take_again": 23.0,
        "difficulty": 4.6
    },
    "raghu_agarwal": {
        "first_name": "Raghu",
        "last_name": "Agarwal",
        "department": "Mechanical Engineering",
        "overall_rating": 1.8,
        "quality": 1.8,
        "num_ratings": 14,
        "would_take_again": 0.0,
        "difficulty": 3.2
    },
    "alireza_mounesisohi": {
        "first_name": "Alireza",
        "last_name": "Mounesisohi",
        "department": "Mechanical Engineering",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 12,
        "would_take_again": 100.0,
        "difficulty": 2.6
    },
    "feruza_amirkulova": {
        "first_name": "Feruza",
        "last_name": "Amirkulova",
        "department": "Mechanical Engineering",
        "overall_rating": 1.9,
        "quality": 1.9,
        "num_ratings": 9,
        "would_take_again": 34.0,
        "difficulty": 4.3
    },
    "art_davis": {
        "first_name": "Art",
        "last_name": "Davis",
        "department": "Electrical Engineering",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 21,
        "would_take_again": 50.0,
        "difficulty": 4.0
    },
    "shahab_ardalan": {
        "first_name": "Shahab",
        "last_name": "Ardalan",
        "department": "Electrical Engineering",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 16,
        "would_take_again": 100.0,
        "difficulty": 3.1
    },
    "avtar_singh": {
        "first_name": "Avtar",
        "last_name": "Singh",
        "department": "Electrical Engineering",
        "overall_rating": 3.2,
        "quality": 3.2,
        "num_ratings": 15,
        "would_take_again": 0.0,
        "difficulty": 3.6
    },
    "muhammad_ali": {
        "first_name": "Muhammad",
        "last_name": "Ali",
        "department": "Electrical Engineering",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 6,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "nitin_aggarwal": {
        "first_name": "Nitin",
        "last_name": "Aggarwal",
        "department": "Business",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 86,
        "would_take_again": 93.0,
        "difficulty": 2.2
    },
    "vivek_agarwal": {
        "first_name": "Vivek",
        "last_name": "Agarwal",
        "department": "Business",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 20,
        "would_take_again": 90.0,
        "difficulty": 2.8
    },
    "anuradha_basu": {
        "first_name": "Anuradha",
        "last_name": "Basu",
        "department": "Business",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 66,
        "would_take_again": 48.0,
        "difficulty": 3.1
    },
    "ashraf_shirani": {
        "first_name": "Ashraf",
        "last_name": "Shirani",
        "department": "Business",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 85,
        "would_take_again": 46.0,
        "difficulty": 2.6
    },
    "leslie_albert": {
        "first_name": "Leslie",
        "last_name": "Albert",
        "department": "Business",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 54,
        "would_take_again": 73.0,
        "difficulty": 2.8
    },
    "asbjorn_osland": {
        "first_name": "Asbjorn",
        "last_name": "Osland",
        "department": "Business",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 93,
        "would_take_again": 80.0,
        "difficulty": 2.5
    },
    "arvinder_loomba": {
        "first_name": "Arvinder",
        "last_name": "Loomba",
        "department": "Business",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 105,
        "would_take_again": 69.0,
        "difficulty": 3.1
    },
    "art_walton": {
        "first_name": "Art",
        "last_name": "Walton",
        "department": "Business",
        "overall_rating": 2.3,
        "quality": 2.3,
        "num_ratings": 80,
        "would_take_again": 100.0,
        "difficulty": 3.7
    },
    "anne_lawrence": {
        "first_name": "Anne",
        "last_name": "Lawrence",
        "department": "Business",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 56,
        "would_take_again": 100.0,
        "difficulty": 2.3
    },
    "yudihishter_ahuja": {
        "first_name": "Yudihishter",
        "last_name": "Ahuja",
        "department": "Business",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 89,
        "would_take_again": 17.0,
        "difficulty": 2.9
    },
    "sulekha_anand": {
        "first_name": "Sulekha",
        "last_name": "Anand",
        "department": "Biology",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 73,
        "would_take_again": 60.0,
        "difficulty": 3.6
    },
    "walter_adams": {
        "first_name": "Walter",
        "last_name": "Adams",
        "department": "Biology",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 9,
        "would_take_again": 100.0,
        "difficulty": 2.9
    },
    "andro_rios": {
        "first_name": "Andro",
        "last_name": "Rios",
        "department": "Chemistry",
        "overall_rating": 4.9,
        "quality": 4.9,
        "num_ratings": 12,
        "would_take_again": 92.0,
        "difficulty": 3.2
    },
    "goretty_alonso": {
        "first_name": "Goretty",
        "last_name": "Alonso",
        "department": "Chemistry",
        "overall_rating": 2.3,
        "quality": 2.3,
        "num_ratings": 38,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "charles_apel": {
        "first_name": "Charles",
        "last_name": "Apel",
        "department": "Chemistry",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 30,
        "would_take_again": 0.0,
        "difficulty": 1.9
    },
    "nargis_adham": {
        "first_name": "Nargis",
        "last_name": "Adham",
        "department": "Physics",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 15,
        "would_take_again": 67.0,
        "difficulty": 2.6
    },
    "andrew_totah_mccarty": {
        "first_name": "Andrew",
        "last_name": "Totah-McCarty",
        "department": "Physics",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 5,
        "would_take_again": 100.0,
        "difficulty": 3.0
    },
    "arlene_asuncion": {
        "first_name": "Arlene",
        "last_name": "Asuncion",
        "department": "Psychology",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 119,
        "would_take_again": 64.0,
        "difficulty": 2.9
    },
    "amy_nguyen": {
        "first_name": "Amy",
        "last_name": "Nguyen",
        "department": "Psychology",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 20,
        "would_take_again": 100.0,
        "difficulty": 1.6
    },
    "amy_caffrey": {
        "first_name": "Amy",
        "last_name": "Caffrey",
        "department": "Psychology",
        "overall_rating": 4.9,
        "quality": 4.9,
        "num_ratings": 15,
        "would_take_again": 100.0,
        "difficulty": 1.7
    },
    "scott_alkire": {
        "first_name": "Scott",
        "last_name": "Alkire",
        "department": "English",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 113,
        "would_take_again": 73.0,
        "difficulty": 2.1
    },
    "adrienne_eastwood": {
        "first_name": "Adrienne",
        "last_name": "Eastwood",
        "department": "English",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 77,
        "would_take_again": 34.0,
        "difficulty": 3.2
    },
    "andy_fleck": {
        "first_name": "Andy",
        "last_name": "Fleck",
        "department": "English",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 55,
        "would_take_again": 0.0,
        "difficulty": 2.9
    },
    "avantika_rohatgi": {
        "first_name": "Avantika",
        "last_name": "Rohatgi",
        "department": "English & Comparative Lit.",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 60,
        "would_take_again": 26.0,
        "difficulty": 3.0
    },
    "allison_gregory": {
        "first_name": "Allison",
        "last_name": "Gregory",
        "department": "English & Comparative Lit.",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 10,
        "would_take_again": 100.0,
        "difficulty": 1.7
    },
    "au_co_tran": {
        "first_name": "Au-Co",
        "last_name": "Tran",
        "department": "English & Comparative Lit.",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 40,
        "would_take_again": 93.0,
        "difficulty": 2.4
    },
    "ume_ali": {
        "first_name": "Ume",
        "last_name": "Ali",
        "department": "English & Comparative Lit.",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 25,
        "would_take_again": 100.0,
        "difficulty": 2.2
    },
    "alicia_hedges": {
        "first_name": "Alicia",
        "last_name": "Hedges",
        "department": "Anthropology",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 25,
        "would_take_again": 92.0,
        "difficulty": 2.2
    },
    "mira_amiras": {
        "first_name": "Mira",
        "last_name": "Amiras",
        "department": "Anthropology",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 27,
        "would_take_again": 0.0,
        "difficulty": 3.6
    },
    "arjun_buxi": {
        "first_name": "Arjun",
        "last_name": "Buxi",
        "department": "Communication Studies",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 31,
        "would_take_again": 90.0,
        "difficulty": 2.0
    },
    "anya_iyengar": {
        "first_name": "Anya",
        "last_name": "Iyengar",
        "department": "Communication Studies",
        "overall_rating": 4.9,
        "quality": 4.9,
        "num_ratings": 97,
        "would_take_again": 99.0,
        "difficulty": 1.6
    },
    "ash_rahmani": {
        "first_name": "Ash",
        "last_name": "Rahmani",
        "department": "Communication Studies",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 4,
        "would_take_again": 100.0,
        "difficulty": 1.5
    },
    "vivian_antonellis": {
        "first_name": "Vivian",
        "last_name": "Antonellis",
        "department": "Communication Studies",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 69,
        "would_take_again": 82.0,
        "difficulty": 2.1
    },
    "amarissa_mathews": {
        "first_name": "Amarissa",
        "last_name": "Mathews",
        "department": "Communication Studies",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 26,
        "would_take_again": 39.0,
        "difficulty": 3.0
    },
    "lark_alder": {
        "first_name": "Lark",
        "last_name": "Alder",
        "department": "Art",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 16,
        "would_take_again": 100.0,
        "difficulty": 1.4
    },
    "andrew_blanton": {
        "first_name": "Andrew",
        "last_name": "Blanton",
        "department": "Art Design",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 4,
        "would_take_again": 75.0,
        "difficulty": 2.3
    },
    "mel_adamson": {
        "first_name": "Mel",
        "last_name": "Adamson",
        "department": "Art & Design",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 20,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "owen_aurelio": {
        "first_name": "Owen",
        "last_name": "Aurelio",
        "department": "Art & Design",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 8,
        "would_take_again": 100.0,
        "difficulty": 3.0
    },
    "arthur_kao": {
        "first_name": "Arthur",
        "last_name": "Kao",
        "department": "Art History",
        "overall_rating": 2.4,
        "quality": 2.4,
        "num_ratings": 42,
        "would_take_again": 0.0,
        "difficulty": 2.9
    },
    "anthony_raynsford": {
        "first_name": "Anthony",
        "last_name": "Raynsford",
        "department": "Art History",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 30,
        "would_take_again": 50.0,
        "difficulty": 2.5
    },
    "amanda_quist": {
        "first_name": "Amanda",
        "last_name": "Quist",
        "department": "Music",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 4,
        "would_take_again": 0.0,
        "difficulty": 2.5
    },
    "aaron_lington": {
        "first_name": "Aaron",
        "last_name": "Lington",
        "department": "Music",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 15,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "kathryn_adduci": {
        "first_name": "Kathryn",
        "last_name": "Adduci",
        "department": "Music",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 26,
        "would_take_again": 100.0,
        "difficulty": 2.4
    },
    "michael_adduci": {
        "first_name": "Michael",
        "last_name": "Adduci",
        "department": "Music",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 13,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "jeremy_abrams": {
        "first_name": "Jeremy",
        "last_name": "Abrams",
        "department": "History",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 37,
        "would_take_again": 82.0,
        "difficulty": 2.5
    },
    "allison_katsev": {
        "first_name": "Allison",
        "last_name": "Katsev",
        "department": "History",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 45,
        "would_take_again": 85.0,
        "difficulty": 2.5
    },
    "apryl_berney": {
        "first_name": "Apryl",
        "last_name": "Berney",
        "department": "History",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 55,
        "would_take_again": 84.0,
        "difficulty": 2.3
    },
    "andrew_delunas": {
        "first_name": "Andrew",
        "last_name": "Delunas",
        "department": "Philosophy",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 51,
        "would_take_again": 93.0,
        "difficulty": 1.5
    },
    "fern_alberts": {
        "first_name": "Fern",
        "last_name": "Alberts",
        "department": "Philosophy",
        "overall_rating": 3.4,
        "quality": 3.4,
        "num_ratings": 72,
        "would_take_again": 42.0,
        "difficulty": 2.7
    },
    "andrew_lavin": {
        "first_name": "Andrew",
        "last_name": "Lavin",
        "department": "Philosophy",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 10,
        "would_take_again": 0.0,
        "difficulty": 2.1
    },
    "alejandra_campos": {
        "first_name": "Alejandra",
        "last_name": "Campos",
        "department": "Spanish",
        "overall_rating": 2.3,
        "quality": 2.3,
        "num_ratings": 7,
        "would_take_again": 15.0,
        "difficulty": 3.9
    },
    "anna_demarchi": {
        "first_name": "Anna",
        "last_name": "Demarchi",
        "department": "French",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 7,
        "would_take_again": 100.0,
        "difficulty": 2.7
    },
    "immene_aggou": {
        "first_name": "Immene",
        "last_name": "Aggou",
        "department": "French",
        "overall_rating": 1.3,
        "quality": 1.3,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "areum_jensen": {
        "first_name": "Areum",
        "last_name": "Jensen",
        "department": "Kinesiology",
        "overall_rating": 1.5,
        "quality": 1.5,
        "num_ratings": 21,
        "would_take_again": 5.0,
        "difficulty": 4.4
    },
    "alev_tug": {
        "first_name": "Alev",
        "last_name": "Tug",
        "department": "Kinesiology",
        "overall_rating": 1.8,
        "quality": 1.8,
        "num_ratings": 13,
        "would_take_again": 16.0,
        "difficulty": 4.0
    },
    "ali_khadem": {
        "first_name": "Ali",
        "last_name": "Khadem",
        "department": "Kinesiology",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 48,
        "would_take_again": 100.0,
        "difficulty": 2.9
    },
    "kathy_abriam_yago": {
        "first_name": "Kathy",
        "last_name": "Abriam-Yago",
        "department": "Nursing",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 12,
        "would_take_again": 0.0,
        "difficulty": 2.8
    },
    "april_wood": {
        "first_name": "April",
        "last_name": "Wood",
        "department": "Nursing",
        "overall_rating": 2.5,
        "quality": 2.5,
        "num_ratings": 15,
        "would_take_again": 17.0,
        "difficulty": 3.6
    },
    "allie_butzlaff": {
        "first_name": "Allie",
        "last_name": "Butzlaff",
        "department": "Nursing",
        "overall_rating": 3.1,
        "quality": 3.1,
        "num_ratings": 7,
        "would_take_again": 58.0,
        "difficulty": 3.9
    },
    "anthony_bernier": {
        "first_name": "Anthony",
        "last_name": "Bernier",
        "department": "Library Science",
        "overall_rating": 2.0,
        "quality": 2.0,
        "num_ratings": 62,
        "would_take_again": 27.0,
        "difficulty": 4.1
    },
    "alison_johnson": {
        "first_name": "Alison",
        "last_name": "Johnson",
        "department": "Library & Information Science",
        "overall_rating": 4.9,
        "quality": 4.9,
        "num_ratings": 25,
        "would_take_again": 96.0,
        "difficulty": 2.7
    },
    "william_armaline": {
        "first_name": "William",
        "last_name": "Armaline",
        "department": "Justice Studies",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 27,
        "would_take_again": 87.0,
        "difficulty": 3.1
    },
    "ericka_adams": {
        "first_name": "Ericka",
        "last_name": "Adams",
        "department": "Justice Studies",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 10,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "drew_todd": {
        "first_name": "Drew",
        "last_name": "Todd",
        "department": "Radio, TV & Film",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 51,
        "would_take_again": 93.0,
        "difficulty": 2.0
    },
    "ashley_seering": {
        "first_name": "Ashley",
        "last_name": "Seering",
        "department": "Radio, TV & Film",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 1.0
    },
    "mike_adams": {
        "first_name": "Mike",
        "last_name": "Adams",
        "department": "Radio, TV & Film",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 13,
        "would_take_again": 0.0,
        "difficulty": 1.8
    },
    "sarah_kate_anderson": {
        "first_name": "Sarah Kate",
        "last_name": "Anderson",
        "department": "Theater",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 41,
        "would_take_again": 55.0,
        "difficulty": 2.7
    },
    "andrea_bechert": {
        "first_name": "Andrea",
        "last_name": "Bechert",
        "department": "Theater",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 6,
        "would_take_again": 84.0,
        "difficulty": 3.2
    },
    "gina_auland": {
        "first_name": "Gina",
        "last_name": "Auland",
        "department": "Dance",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "philip_agyapong": {
        "first_name": "Philip",
        "last_name": "Agyapong",
        "department": "Dance",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "alexander_gershenson": {
        "first_name": "Alexander",
        "last_name": "Gershenson",
        "department": "Environmental Studies",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 30,
        "would_take_again": 0.0,
        "difficulty": 3.3
    },
    "ada_marquez": {
        "first_name": "Ada",
        "last_name": "Marquez",
        "department": "Environmental Studies",
        "overall_rating": 3.4,
        "quality": 3.4,
        "num_ratings": 28,
        "would_take_again": 73.0,
        "difficulty": 3.2
    },
    "walter_arenstein": {
        "first_name": "Walter",
        "last_name": "Arenstein",
        "department": "Environmental Studies",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 9,
        "would_take_again": 0.0,
        "difficulty": 2.6
    },
    "asha_weinstein": {
        "first_name": "Asha",
        "last_name": "Weinstein",
        "department": "Urban Planning",
        "overall_rating": 2.2,
        "quality": 2.2,
        "num_ratings": 7,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "andrea_whitson": {
        "first_name": "Andrea",
        "last_name": "Whitson",
        "department": "Nutrition & Foods",
        "overall_rating": 3.2,
        "quality": 3.2,
        "num_ratings": 42,
        "would_take_again": 54.0,
        "difficulty": 2.9
    },
    "ashwini_wagle": {
        "first_name": "Ashwini",
        "last_name": "Wagle",
        "department": "Nutrition & Foods",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 33,
        "would_take_again": 100.0,
        "difficulty": 1.9
    },
    "ashlee_gossard": {
        "first_name": "Ashlee",
        "last_name": "Gossard",
        "department": "Nutrition & Foods",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 17,
        "would_take_again": 71.0,
        "difficulty": 2.7
    },
    "andrea_rowell": {
        "first_name": "Andrea",
        "last_name": "Rowell",
        "department": "Nutrition & Foods",
        "overall_rating": 3.4,
        "quality": 3.4,
        "num_ratings": 8,
        "would_take_again": 0.0,
        "difficulty": 4.4
    },
    "alan_finkelstein": {
        "first_name": "Alan",
        "last_name": "Finkelstein",
        "department": "Nutrition & Foods",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 26,
        "would_take_again": 100.0,
        "difficulty": 1.8
    },
    "roberta_ahlquist": {
        "first_name": "Roberta",
        "last_name": "Ahlquist",
        "department": "Secondary Education",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 41,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "alexander_sapiens": {
        "first_name": "Alexander",
        "last_name": "Sapiens",
        "department": "Education",
        "overall_rating": 2.7,
        "quality": 2.7,
        "num_ratings": 14,
        "would_take_again": 0.0,
        "difficulty": 2.4
    },
    "amy_strage": {
        "first_name": "Amy",
        "last_name": "Strage",
        "department": "Education",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 48,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "angela_rickford": {
        "first_name": "Angela",
        "last_name": "Rickford",
        "department": "Education",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 8,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "amanda_barden": {
        "first_name": "Amanda",
        "last_name": "Barden",
        "department": "Social Work",
        "overall_rating": 1.0,
        "quality": 1.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "alen_yaghoubi": {
        "first_name": "Alen",
        "last_name": "Yaghoubi",
        "department": "Counselor Education",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 9,
        "would_take_again": 78.0,
        "difficulty": 1.1
    },
    "amna_jaffer": {
        "first_name": "Amna",
        "last_name": "Jaffer",
        "department": "Counselor Education",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 20,
        "would_take_again": 95.0,
        "difficulty": 1.7
    },
    "lewis_aptekar": {
        "first_name": "Lewis",
        "last_name": "Aptekar",
        "department": "Counselor Education",
        "overall_rating": 2.8,
        "quality": 2.8,
        "num_ratings": 6,
        "would_take_again": 0.0,
        "difficulty": 1.8
    },
    "aaa_aaa": {
        "first_name": "aaa",
        "last_name": "aaa",
        "department": "Computer Science",
        "overall_rating": 2.6,
        "quality": 2.6,
        "num_ratings": 40,
        "would_take_again": 50.0,
        "difficulty": 4.4
    },
    "ann_kalinowski": {
        "first_name": "Ann",
        "last_name": "Kalinowski",
        "department": "Business",
        "overall_rating": 2.6,
        "quality": 2.6,
        "num_ratings": 199,
        "would_take_again": 35.0,
        "difficulty": 3.8
    },
    "ravi_agarwal": {
        "first_name": "Ravi",
        "last_name": "Agarwal",
        "department": "Marketing",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 6,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "ron_pasek": {
        "first_name": "Ron",
        "last_name": "Pasek",
        "department": "Accounting & Finance",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 8,
        "would_take_again": 63.0,
        "difficulty": 4.5
    },
    "dominic_abucejo": {
        "first_name": "Dominic",
        "last_name": "Abucejo",
        "department": "Computer Science",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 20,
        "would_take_again": 82.0,
        "difficulty": 2.3
    },
    "ali_mehran": {
        "first_name": "Ali",
        "last_name": "Mehran",
        "department": "Engineering",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 4,
        "would_take_again": 75.0,
        "difficulty": 3.5
    },
    "jesus_aguilar": {
        "first_name": "Jesus",
        "last_name": "Aguilar",
        "department": "Photography",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "atom_murata": {
        "first_name": "Atom",
        "last_name": "Murata",
        "department": "Accounting & Finance",
        "overall_rating": 2.8,
        "quality": 2.8,
        "num_ratings": 5,
        "would_take_again": 40.0,
        "difficulty": 3.6
    },
    "armin_moghadam": {
        "first_name": "Armin",
        "last_name": "Moghadam",
        "department": "Technology",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 10,
        "would_take_again": 80.0,
        "difficulty": 3.2
    },
    "ahmed_banafa": {
        "first_name": "Ahmed",
        "last_name": "Banafa",
        "department": "Engineering",
        "overall_rating": 4.9,
        "quality": 4.9,
        "num_ratings": 36,
        "would_take_again": 98.0,
        "difficulty": 2.2
    },
    "alla_petrosyan": {
        "first_name": "Alla",
        "last_name": "Petrosyan",
        "department": "Engineering",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 7,
        "would_take_again": 58.0,
        "difficulty": 1.9
    },
    "wahida_akter": {
        "first_name": "Wahida",
        "last_name": "Akter",
        "department": "Biology",
        "overall_rating": 2.3,
        "quality": 2.3,
        "num_ratings": 3,
        "would_take_again": 67.0,
        "difficulty": 3.0
    },
    "arthur_casey": {
        "first_name": "Arthur",
        "last_name": "Casey",
        "department": "Business",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 44,
        "would_take_again": 92.0,
        "difficulty": 1.8
    },
    "ahmad_shaar": {
        "first_name": "Ahmad",
        "last_name": "Shaar",
        "department": "Business",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 38,
        "would_take_again": 93.0,
        "difficulty": 2.1
    },
    "stephen_artim": {
        "first_name": "Stephen",
        "last_name": "Artim",
        "department": "Business",
        "overall_rating": 1.6,
        "quality": 1.6,
        "num_ratings": 16,
        "would_take_again": 13.0,
        "difficulty": 4.4
    },
    "ash_padwal": {
        "first_name": "Ash",
        "last_name": "Padwal",
        "department": "Business",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 7,
        "would_take_again": 72.0,
        "difficulty": 2.1
    },
    "amith_belman": {
        "first_name": "Amith",
        "last_name": "Belman",
        "department": "Computer Science",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 6,
        "would_take_again": 100.0,
        "difficulty": 2.8
    },
    "mohammed_ameen": {
        "first_name": "Mohammed",
        "last_name": "Ameen",
        "department": "Mechanical Engineering",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "regina_arnold": {
        "first_name": "Regina",
        "last_name": "Arnold",
        "department": "English & Comparative Lit.",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 8,
        "would_take_again": 100.0,
        "difficulty": 2.5
    },
    "alicia_mullens": {
        "first_name": "Alicia",
        "last_name": "Mullens",
        "department": "Meteorology",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 33,
        "would_take_again": 97.0,
        "difficulty": 1.9
    },
    "adam_kochanski": {
        "first_name": "Adam",
        "last_name": "Kochanski",
        "department": "Meteorology",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 9,
        "would_take_again": 89.0,
        "difficulty": 2.6
    },
    "areana_flores": {
        "first_name": "Areana",
        "last_name": "Flores",
        "department": "Meteorology",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 1.0
    },
    "d_andersen": {
        "first_name": "D",
        "last_name": "Andersen",
        "department": "Geology",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 24,
        "would_take_again": 0.0,
        "difficulty": 2.8
    },
    "anthony_earls": {
        "first_name": "Anthony",
        "last_name": "Earls",
        "department": "Geology",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "anthony_lenci": {
        "first_name": "Anthony",
        "last_name": "Lenci",
        "department": "Geology",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "ajay_fay": {
        "first_name": "Ajay",
        "last_name": "Fay",
        "department": "Photography",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 4.0
    },
    "abigail_nuno": {
        "first_name": "Abigail",
        "last_name": "Nuno",
        "department": "Communication",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "kelley_abrams": {
        "first_name": "Kelley",
        "last_name": "Abrams",
        "department": "Child Development",
        "overall_rating": 1.9,
        "quality": 1.9,
        "num_ratings": 5,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "allison_smith": {
        "first_name": "Allison",
        "last_name": "Smith",
        "department": "Occupational Therapy",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "tziva_abramson": {
        "first_name": "Tziva",
        "last_name": "Abramson",
        "department": "Biology",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 5,
        "would_take_again": 0.0,
        "difficulty": 2.4
    },
    "russell_arias": {
        "first_name": "Russell",
        "last_name": "Arias",
        "department": "Psychology",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 81,
        "would_take_again": 100.0,
        "difficulty": 1.8
    },
    "patricia_aubel": {
        "first_name": "Patricia",
        "last_name": "Aubel",
        "department": "Mathematics",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 4,
        "would_take_again": 100.0,
        "difficulty": 1.7
    },
    "andrew_smith": {
        "first_name": "Andrew",
        "last_name": "Smith",
        "department": "Biology",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 3,
        "would_take_again": 100.0,
        "difficulty": 3.0
    },
    "thadeus_aid": {
        "first_name": "Thadeus",
        "last_name": "Aid",
        "department": "Computer Science",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 5.0
    },
    "marilyn_ampuero": {
        "first_name": "Marilyn",
        "last_name": "Ampuero",
        "department": "Psychology",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 2.7
    },
    "deolinda_adao": {
        "first_name": "Deolinda",
        "last_name": "Adao",
        "department": "Spanish",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 2.5
    },
    "saurabh_agarwal": {
        "first_name": "Saurabh",
        "last_name": "Agarwal",
        "department": "Computer Engineering",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "shelley_ash": {
        "first_name": "Shelley",
        "last_name": "Ash",
        "department": "Health Science",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 16,
        "would_take_again": 0.0,
        "difficulty": 2.5
    },
    "noel_arbabaraghi": {
        "first_name": "Noel",
        "last_name": "Arbabaraghi",
        "department": "Child Development",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 1.0
    },
    "anjali_dutt": {
        "first_name": "Anjali",
        "last_name": "Dutt",
        "department": "Women's Studies",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "anne_fountain": {
        "first_name": "Anne",
        "last_name": "Fountain",
        "department": "Spanish",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 17,
        "would_take_again": 0.0,
        "difficulty": 2.5
    },
    "amy_chan": {
        "first_name": "Amy",
        "last_name": "Chan",
        "department": "Health Science",
        "overall_rating": 2.7,
        "quality": 2.7,
        "num_ratings": 6,
        "would_take_again": 0.0,
        "difficulty": 4.5
    },
    "albert_gonzalez": {
        "first_name": "Albert",
        "last_name": "Gonzalez",
        "department": "Anthropology",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "angela_rickford": {
        "first_name": "Angela",
        "last_name": "Rickford",
        "department": "Education",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 8,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "kate_antosik_parsons": {
        "first_name": "Kate",
        "last_name": "Antosik-Parsons",
        "department": "Geography",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "amy_leisenring": {
        "first_name": "Amy",
        "last_name": "Leisenring",
        "department": "Sociology",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 38,
        "would_take_again": 0.0,
        "difficulty": 2.6
    },
    "ali_reza": {
        "first_name": "Ali",
        "last_name": "Reza",
        "department": "Accounting",
        "overall_rating": 2.6,
        "quality": 2.6,
        "num_ratings": 98,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "alice_carter": {
        "first_name": "Alice",
        "last_name": "Carter",
        "department": "Art & Design",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 14,
        "would_take_again": 0.0,
        "difficulty": 4.4
    },
    "dean_adachi": {
        "first_name": "Dean",
        "last_name": "Adachi",
        "department": "Asian American Studies",
        "overall_rating": 1.5,
        "quality": 1.5,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "ashley_davis": {
        "first_name": "Ashley",
        "last_name": "Davis",
        "department": "Accounting",
        "overall_rating": 3.2,
        "quality": 3.2,
        "num_ratings": 15,
        "would_take_again": 0.0,
        "difficulty": 3.1
    },
    "andrew_campbell": {
        "first_name": "Andrew",
        "last_name": "Campbell",
        "department": "Biology",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "andrew_altschul": {
        "first_name": "Andrew",
        "last_name": "Altschul",
        "department": "English & Comparative Lit.",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "amy_resnick": {
        "first_name": "Amy",
        "last_name": "Resnick",
        "department": "Theater",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 4,
        "would_take_again": 0.0,
        "difficulty": 1.5
    },
    "sina_aboutorabi": {
        "first_name": "Sina",
        "last_name": "Aboutorabi",
        "department": "Technology",
        "overall_rating": 2.2,
        "quality": 2.2,
        "num_ratings": 10,
        "would_take_again": 30.0,
        "difficulty": 3.5
    },
    "radha_aravamudhan": {
        "first_name": "Radha",
        "last_name": "Aravamudhan",
        "department": "Aerospace Studies",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 5,
        "would_take_again": 100.0,
        "difficulty": 2.0
    },
    "susan_ahmed": {
        "first_name": "Susan",
        "last_name": "Ahmed",
        "department": "Aerospace Studies",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "alison_white": {
        "first_name": "Alison",
        "last_name": "White",
        "department": "Kinesiology",
        "overall_rating": 2.5,
        "quality": 2.5,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "ali_rejaie": {
        "first_name": "Ali",
        "last_name": "Rejaie",
        "department": "Engineering",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 5,
        "would_take_again": 0.0,
        "difficulty": 3.8
    },
    "anuradha_meenakshisundaram": {
        "first_name": "Anuradha",
        "last_name": "Meenakshisundaram",
        "department": "Chemistry",
        "overall_rating": 2.5,
        "quality": 2.5,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "avila_rocio": {
        "first_name": "Avila",
        "last_name": "Rocio",
        "department": "Computer Science",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 1.0
    },
    "allison_charland": {
        "first_name": "Allison",
        "last_name": "Charland",
        "department": "Meteorology",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 1.0
    },
    "janet_anaya": {
        "first_name": "Janet",
        "last_name": "Anaya",
        "department": "Business",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 115,
        "would_take_again": 0.0,
        "difficulty": 3.4
    },
    "mel_adamson": {
        "first_name": "Mel",
        "last_name": "Adamson",
        "department": "Art & Design",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 20,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "augstin_araya": {
        "first_name": "Augstin",
        "last_name": "Araya",
        "department": "Computer Science",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 39,
        "would_take_again": 0.0,
        "difficulty": 3.2
    },
    "brandon_atkins": {
        "first_name": "Brandon",
        "last_name": "Atkins",
        "department": "Philosophy",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "andrew_maul": {
        "first_name": "Andrew",
        "last_name": "Maul",
        "department": "Mathematics",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "ajaib_bansal": {
        "first_name": "Ajaib",
        "last_name": "Bansal",
        "department": "Mechanical Engineering",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "charanya_arjun": {
        "first_name": "Charanya",
        "last_name": "Arjun",
        "department": "English",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 8,
        "would_take_again": 0.0,
        "difficulty": 3.1
    },
    "a_s_bansal": {
        "first_name": "A S",
        "last_name": "Bansal",
        "department": "Mechanical Engineering",
        "overall_rating": 1.3,
        "quality": 1.3,
        "num_ratings": 4,
        "would_take_again": 0.0,
        "difficulty": 4.5
    },
    "anitarani_chinthalapati": {
        "first_name": "Anitarani",
        "last_name": "Chinthalapati",
        "department": "Mathematics",
        "overall_rating": 2.5,
        "quality": 2.5,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "arthur_kao": {
        "first_name": "Arthur",
        "last_name": "Kao",
        "department": "Art History",
        "overall_rating": 2.4,
        "quality": 2.4,
        "num_ratings": 42,
        "would_take_again": 0.0,
        "difficulty": 2.9
    },
    "afshin_tiraie": {
        "first_name": "Afshin",
        "last_name": "Tiraie",
        "department": "Mathematics",
        "overall_rating": 1.4,
        "quality": 1.4,
        "num_ratings": 9,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "ahmed_eddie_nazzal": {
        "first_name": "Ahmed Eddie",
        "last_name": "Nazzal",
        "department": "Biology",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 1.5
    },
    "lynne_andonian": {
        "first_name": "Lynne",
        "last_name": "Andonian",
        "department": "Occupational Therapy",
        "overall_rating": 2.8,
        "quality": 2.8,
        "num_ratings": 16,
        "would_take_again": 0.0,
        "difficulty": 3.4
    },
    "anu_bullis": {
        "first_name": "Anu",
        "last_name": "Bullis",
        "department": "Business",
        "overall_rating": 2.5,
        "quality": 2.5,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 3.7
    },
    "allison_winston": {
        "first_name": "Allison",
        "last_name": "Winston",
        "department": "English",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 17,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "david_asquith": {
        "first_name": "David",
        "last_name": "Asquith",
        "department": "Sociology",
        "overall_rating": 3.4,
        "quality": 3.4,
        "num_ratings": 29,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "rocio_avila": {
        "first_name": "Rocio",
        "last_name": "Avila",
        "department": "Science",
        "overall_rating": 2.3,
        "quality": 2.3,
        "num_ratings": 6,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "sundararajan_arabhi": {
        "first_name": "Sundararajan",
        "last_name": "Arabhi",
        "department": "Mathematics",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 33,
        "would_take_again": 0.0,
        "difficulty": 3.4
    },
    "janene_argel": {
        "first_name": "Janene",
        "last_name": "Argel",
        "department": "Child Development",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 27,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "andrew_tucker": {
        "first_name": "Andrew",
        "last_name": "Tucker",
        "department": "English & Comparative Lit.",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "anne_may_navarette": {
        "first_name": "Anne May",
        "last_name": "Navarette",
        "department": "Communication Studies",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 14,
        "would_take_again": 0.0,
        "difficulty": 2.5
    },
    "aaron_lington": {
        "first_name": "Aaron",
        "last_name": "Lington",
        "department": "Music",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 15,
        "would_take_again": 0.0,
        "difficulty": 2.3
    },
    "genelle_austin_lett": {
        "first_name": "Genelle",
        "last_name": "Austin-Lett",
        "department": "Communication",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 38,
        "would_take_again": 0.0,
        "difficulty": 2.8
    },
    "anna_le": {
        "first_name": "Anna",
        "last_name": "LE",
        "department": "Not Specified",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "victoria_arafa": {
        "first_name": "Victoria",
        "last_name": "Arafa",
        "department": "Communication",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "john_athanasiou": {
        "first_name": "John",
        "last_name": "Athanasiou",
        "department": "Engineering",
        "overall_rating": 3.7,
        "quality": 3.7,
        "num_ratings": 50,
        "would_take_again": 0.0,
        "difficulty": 1.8
    },
    "amanda_moore": {
        "first_name": "Amanda",
        "last_name": "Moore",
        "department": "English & Comparative Lit.",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 2.0
    },
    "al_chen": {
        "first_name": "AL",
        "last_name": "Chen",
        "department": "Mathematics",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 3,
        "would_take_again": 0.0,
        "difficulty": 1.0
    },
    "andy_fleck": {
        "first_name": "Andy",
        "last_name": "Fleck",
        "department": "English",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 55,
        "would_take_again": 0.0,
        "difficulty": 2.9
    },
    "amy_dreiling": {
        "first_name": "Amy",
        "last_name": "Dreiling",
        "department": "Mathematics",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 5,
        "would_take_again": 0.0,
        "difficulty": 2.4
    },
    "charlene_archibeque": {
        "first_name": "Charlene",
        "last_name": "Archibeque",
        "department": "Music",
        "overall_rating": 3.4,
        "quality": 3.4,
        "num_ratings": 5,
        "would_take_again": 0.0,
        "difficulty": 3.0
    },
    "gilberto_arriaza": {
        "first_name": "Gilberto",
        "last_name": "Arriaza",
        "department": "Educational Leadership",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "ary_chernomorsky": {
        "first_name": "Ary",
        "last_name": "Chernomorsky",
        "department": "Engineering",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 4,
        "would_take_again": 0.0,
        "difficulty": 3.5
    },
    "alexander_sapiens": {
        "first_name": "Alexander",
        "last_name": "Sapiens",
        "department": "Education",
        "overall_rating": 2.7,
        "quality": 2.7,
        "num_ratings": 14,
        "would_take_again": 0.0,
        "difficulty": 2.4
    },
    "amanda_quist": {
        "first_name": "Amanda",
        "last_name": "Quist",
        "department": "Music",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 4,
        "would_take_again": 0.0,
        "difficulty": 2.5
    },
    "gina_auland": {
        "first_name": "Gina",
        "last_name": "Auland",
        "department": "Dance",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 2,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "audrey_chan": {
        "first_name": "Audrey",
        "last_name": "Chan",
        "department": "Mathematics",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 5,
        "would_take_again": 80.0,
        "difficulty": 3.4
    },
    "abbas_moallem": {
        "first_name": "Abbas",
        "last_name": "Moallem",
        "department": "Industrial Engineering",
        "overall_rating": 1.9,
        "quality": 1.9,
        "num_ratings": 39,
        "would_take_again": 24.0,
        "difficulty": 3.6
    },
    "alissa_shaw": {
        "first_name": "Alissa",
        "last_name": "Shaw",
        "department": "Health Science",
        "overall_rating": 2.7,
        "quality": 2.7,
        "num_ratings": 99,
        "would_take_again": 36.0,
        "difficulty": 3.9
    },
    "alayna_mills": {
        "first_name": "Alayna",
        "last_name": "Mills",
        "department": "English & Comparative Lit.",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 14,
        "would_take_again": 58.0,
        "difficulty": 2.5
    },
    "amarissa_mathews": {
        "first_name": "Amarissa",
        "last_name": "Mathews",
        "department": "Communication Studies",
        "overall_rating": 2.9,
        "quality": 2.9,
        "num_ratings": 26,
        "would_take_again": 39.0,
        "difficulty": 3.0
    },
    "arthur_zarate": {
        "first_name": "Arthur",
        "last_name": "Zarate",
        "department": "Humanities",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 9,
        "would_take_again": 67.0,
        "difficulty": 2.9
    },
    "ashley_seering": {
        "first_name": "Ashley",
        "last_name": "Seering",
        "department": "Radio, TV & Film",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 1.0
    },
    "ayam_nouiouat": {
        "first_name": "Ayam",
        "last_name": "Nouiouat",
        "department": "Health Science",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 4.0
    },
    "mary_ann_harlan": {
        "first_name": "Mary Ann",
        "last_name": "Harlan",
        "department": "Library Science",
        "overall_rating": 3.6,
        "quality": 3.6,
        "num_ratings": 11,
        "would_take_again": 80.0,
        "difficulty": 3.6
    },
    "bud_ayers": {
        "first_name": "Bud",
        "last_name": "Ayers",
        "department": "Kinesiology",
        "overall_rating": 4.0,
        "quality": 4.0,
        "num_ratings": 83,
        "would_take_again": 65.0,
        "difficulty": 1.9
    },
    "owen_aurelio": {
        "first_name": "Owen",
        "last_name": "Aurelio",
        "department": "Art & Design",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 8,
        "would_take_again": 100.0,
        "difficulty": 3.0
    },
    "benjamin_reed": {
        "first_name": "Benjamin",
        "last_name": "Reed",
        "department": "Computer Science",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 45,
        "would_take_again": 95.0,
        "difficulty": 3.2,
        "contact": {
            "email": "ben.reed@sjsu.edu",
            "office": "MQH 232",
            "office_hours": "Tue/Thu 2:00-3:00pm",
            "phone": "(408) 924-5174",
            "website": "https://www.cs.sjsu.edu/~reed/"
        },
        "academic": {
            "title": "Professor",
            "research_interests": ["Distributed Systems", "Cloud Computing", "Big Data"],
            "current_courses": ["CS149", "CS249", "CS259"]
        },
    },
    "bill_andreopoulos": {
        "first_name": "Bill",
        "last_name": "Andreopoulos",
        "department": "Computer Science",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 35,
        "would_take_again": 80.0,
        "difficulty": 3.2
    },
    "bruce_olszewski": {
        "first_name": "Bruce",
        "last_name": "Olszewski",
        "department": "Environmental Studies",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 42,
        "would_take_again": 89.0,
        "difficulty": 2.8
    },
    "brian_murphy": {
        "first_name": "Brian",
        "last_name": "Murphy",
        "department": "Political Science",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 15,
        "would_take_again": 87.0,
        "difficulty": 2.5
    },
    "barbara_conry": {
        "first_name": "Barbara",
        "last_name": "Conry",
        "department": "Kinesiology",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 89,
        "would_take_again": 82.0,
        "difficulty": 2.1
    },
    "bethany_shifflett": {
        "first_name": "Bethany",
        "last_name": "Shifflett",
        "department": "Kinesiology",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 76,
        "would_take_again": 75.0,
        "difficulty": 2.4
    },
    "bradley_stone": {
        "first_name": "Bradley",
        "last_name": "Stone",
        "department": "Chemistry",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 92,
        "would_take_again": 88.0,
        "difficulty": 2.8
    },
    "ben_reed": {
        "first_name": "Ben",
        "last_name": "Reed",
        "department": "Computer Science",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 45,
        "would_take_again": 95.0,
        "difficulty": 3.2
    },
    "bryan_stevenson": {
        "first_name": "Bryan",
        "last_name": "Stevenson",
        "department": "Computer Science",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 28,
        "would_take_again": 89.0,
        "difficulty": 3.1
    },
    "bill_wilson": {
        "first_name": "Bill",
        "last_name": "Wilson",
        "department": "Computer Science",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 32,
        "would_take_again": 82.0,
        "difficulty": 3.4
    },
    "bob_chun": {
        "first_name": "Bob",
        "last_name": "Chun",
        "department": "Computer Science",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 89,
        "would_take_again": 91.0,
        "difficulty": 3.3
    },
    "brent_duckor": {
        "first_name": "Brent",
        "last_name": "Duckor",
        "department": "Education",
        "overall_rating": 2.8,
        "quality": 2.8,
        "num_ratings": 45,
        "would_take_again": 33.0,
        "difficulty": 3.5
    },
    "brian_bornstein": {
        "first_name": "Brian",
        "last_name": "Bornstein",
        "department": "Mathematics",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 38,
        "would_take_again": 82.0,
        "difficulty": 2.8
    },
    "bernadette_cheyne": {
        "first_name": "Bernadette",
        "last_name": "Cheyne",
        "department": "Theater Arts",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 29,
        "would_take_again": 67.0,
        "difficulty": 2.5
    },
    "brian_thoms": {
        "first_name": "Brian",
        "last_name": "Thoms",
        "department": "Computer Science",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 15,
        "would_take_again": 87.0,
        "difficulty": 2.8
    },
    "boris_kiefer": {
        "first_name": "Boris",
        "last_name": "Kiefer",
        "department": "Physics",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 42,
        "would_take_again": 65.0,
        "difficulty": 3.5
    },
    "beverly_grindstaff": {
        "first_name": "Beverly",
        "last_name": "Grindstaff",
        "department": "Art History",
        "overall_rating": 3.2,
        "quality": 3.2,
        "num_ratings": 31,
        "would_take_again": 45.0,
        "difficulty": 3.1
    },
    "brian_taylor": {
        "first_name": "Brian",
        "last_name": "Taylor",
        "department": "Art & Design",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 25,
        "would_take_again": 92.0,
        "difficulty": 2.2
    },
    "baba_kofi_weusijana": {
        "first_name": "Baba Kofi",
        "last_name": "Weusijana",
        "department": "Education",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 18,
        "would_take_again": 78.0,
        "difficulty": 2.4
    },
    "brandon_white": {
        "first_name": "Brandon",
        "last_name": "White",
        "department": "Biology",
        "overall_rating": 4.4,
        "quality": 4.4,
        "num_ratings": 45,
        "would_take_again": 85.0,
        "difficulty": 2.9
    },
    "barbara_conry": {
        "first_name": "Barbara",
        "last_name": "Conry",
        "department": "Kinesiology",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 89,
        "would_take_again": 82.0,
        "difficulty": 2.1
    },
    "brian_peterson": {
        "first_name": "Brian",
        "last_name": "Peterson",
        "department": "Mathematics",
        "overall_rating": 4.8,
        "quality": 4.8,
        "num_ratings": 52,
        "would_take_again": 94.0,
        "difficulty": 2.5
    },
    "benjamin_carter": {
        "first_name": "Benjamin",
        "last_name": "Carter",
        "department": "Anthropology",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 28,
        "would_take_again": 89.0,
        "difficulty": 2.8
    },
    "brian_cantwell": {
        "first_name": "Brian",
        "last_name": "Cantwell",
        "department": "History",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 35,
        "would_take_again": 88.0,
        "difficulty": 2.7
    },
    "barry_andrews": {
        "first_name": "Barry",
        "last_name": "Andrews",
        "department": "Psychology",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 42,
        "would_take_again": 85.0,
        "difficulty": 2.5
    },
    "bonita_cox": {
        "first_name": "Bonita",
        "last_name": "Cox",
        "department": "Business",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 65,
        "would_take_again": 72.0,
        "difficulty": 3.1
    },
    "bruce_goldman": {
        "first_name": "Bruce",
        "last_name": "Goldman",
        "department": "English",
        "overall_rating": 4.6,
        "quality": 4.6,
        "num_ratings": 28,
        "would_take_again": 92.0,
        "difficulty": 2.4
    },
    "catherine_voss": {
        "first_name": "Catherine",
        "last_name": "Voss",
        "department": "Computer Science",
        "overall_rating": 4.3,
        "quality": 4.3,
        "num_ratings": 28,
        "would_take_again": 85.0,
        "difficulty": 3.2
    },
    "david_taylor": {
        "first_name": "David",
        "last_name": "Taylor",
        "department": "Computer Science",
        "overall_rating": 4.7,
        "quality": 4.7,
        "num_ratings": 42,
        "would_take_again": 92.0,
        "difficulty": 2.8
    },
    "chris_pollett": {
        "first_name": "Chris",
        "last_name": "Pollett",
        "department": "Computer Science",
        "overall_rating": 3.3,
        "num_ratings": 64,
        "would_take_again": 53.0,
        "difficulty": 3.7,
        "tags": [
            "GET READY TO READ",
            "TOUGH GRADER",
            "EXTRA CREDIT",
            "LOTS OF HOMEWORK",
            "CLEAR GRADING CRITERIA"
        ],
        "rating_distribution": {
            "5": 18,
            "4": 18,
            "3": 12,
            "2": 6,
            "1": 10
        },
        "courses": ["CS152", "CS154", "CS156", "CS157A", "CS157B", "CS158A", "CS174", "CS256", "CS257", "CS267"],
        "teaching_style": [
            "Dense lecture slides",
            "Weekly quizzes",
            "In-class activities",
            "Heavy memorization focus",
            "Group work allowed",
            "Recorded lectures available",
            "Significant safety nets"
        ],
        "notes": [
            "Mixed reviews on teaching effectiveness",
            "Generous curves noted",
            "Reuses exam questions",
            "Heavy workload in assignments",
            "Strong theoretical focus",
            "Accessible in office hours",
            "Passing grade at 55%"
        ]
    },
    "jon_pearce": {
        "first_name": "Jon",
        "last_name": "Pearce",
        "department": "Computer Science",
        "overall_rating": 3.9,
        "quality": 3.9,
        "num_ratings": 65,
        "would_take_again": 71.0,
        "difficulty": 3.4
    },
    "michael_finder": {
        "first_name": "Michael",
        "last_name": "Finder",
        "department": "Computer Science",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 42,
        "would_take_again": 82.0,
        "difficulty": 2.9
    },
    "sami_khuri": {
        "first_name": "Sami",
        "last_name": "Khuri",
        "department": "Computer Science",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 89,
        "would_take_again": 65.0,
        "difficulty": 3.7
    },
    "melody_moh": {
        "first_name": "Melody",
        "last_name": "Moh",
        "department": "Computer Science",
        "overall_rating": 3.2,
        "quality": 3.2,
        "num_ratings": 82,
        "would_take_again": 45.0,
        "difficulty": 3.8
    },
    "teng_moh": {
        "first_name": "Teng",
        "last_name": "Moh",
        "department": "Computer Science",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 75,
        "would_take_again": 52.0,
        "difficulty": 3.6
    },
    "mike_wu": {
        "first_name": "Mike",
        "last_name": "Wu",
        "department": "Computer Science",
        "overall_rating": 4.2,
        "quality": 4.2,
        "num_ratings": 45,
        "would_take_again": 82.0,
        "difficulty": 3.1
    },
    "robert_chun": {
        "first_name": "Robert",
        "last_name": "Chun",
        "department": "Computer Science",
        "overall_rating": 4.2,
        "num_ratings": 48,
        "would_take_again": 60.0,
        "difficulty": 3.0,
        "tags": [
            "AMAZING LECTURES",
            "RESPECTED",
            "CARING",
            "TOUGH GRADER",
            "WOULD TAKE AGAIN"
        ],
        "rating_distribution": {
            "5": 33,
            "4": 7,
            "3": 2,
            "2": 3,
            "1": 3
        },
        "courses": ["CS147", "CS149", "CS159", "CS247", "CS259"],
        "teaching_style": [
            "Organized lecture notes",
            "Clear presentations",
            "Pre-recorded lectures available",
            "Student presentations component",
            "Limited assignments",
            "Test-focused assessment",
            "No textbook required"
        ],
        "notes": [
            "Mixed reviews on grading fairness",
            "Reuses course materials",
            "Strong focus on lecture notes",
            "Long but comprehensive exams",
            "Calm teaching style",
            "Same material for grad/undergrad courses",
            "Email response issues noted"
        ]
    },
    "chung_wen_tsao": {
        "first_name": "Chung-Wen",
        "last_name": "Tsao",
        "department": "Computer Science",
        "overall_rating": 2.1,
        "quality": 2.1,
        "num_ratings": 67,
        "would_take_again": 29.0,
        "difficulty": 3.5
    },
    "navrati_saxena": {
        "first_name": "Navrati",
        "last_name": "Saxena",
        "department": "Computer Science",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 33,
        "would_take_again": 82.0,
        "difficulty": 3.1
    },
    "genya_ishigaki": {
        "first_name": "Genya",
        "last_name": "Ishigaki",
        "department": "Computer Science",
        "overall_rating": 4.1,
        "quality": 4.1,
        "num_ratings": 9,
        "would_take_again": 78.0,
        "difficulty": 3.1
    },
    "mira_jane": {
        "first_name": "Mira",
        "last_name": "Jane",
        "department": "Computer Science",
        "overall_rating": 1.1,
        "quality": 1.1,
        "num_ratings": 9,
        "would_take_again": 0.0,
        "difficulty": 4.8
    },
    "prateek_jain": {
        "first_name": "Prateek",
        "last_name": "Jain",
        "department": "Computer Science",
        "overall_rating": 1.9,
        "quality": 1.9,
        "num_ratings": 9,
        "would_take_again": 23.0,
        "difficulty": 3.8
    },
    "vijay_eranti": {
        "first_name": "Vijay",
        "last_name": "Eranti",
        "department": "Computer Science",
        "overall_rating": 1.0,
        "quality": 1.0,
        "num_ratings": 1,
        "would_take_again": 0.0,
        "difficulty": 4.0
    },
    "suneuy_kim": {
        "first_name": "Suneuy",
        "last_name": "Kim",
        "department": "Computer Science",
        "overall_rating": 3.8,
        "quality": 3.8,
        "num_ratings": 100,
        "would_take_again": 65.0,
        "difficulty": 3.6
    },
    "kaushik_patra": {
        "first_name": "Kaushik",
        "last_name": "Patra",
        "department": "Computer Science",
        "overall_rating": 2.4,
        "quality": 2.4,
        "num_ratings": 39,
        "would_take_again": 29.0,
        "difficulty": 4.3
    },
    "faramarz_mortezaie": {
        "first_name": "Faramarz",
        "last_name": "Mortezaie",
        "department": "Computer Science",
        "overall_rating": 3.5,
        "quality": 3.5,
        "num_ratings": 52,
        "would_take_again": 70.0,
        "difficulty": 3.0
    },
    "yan_chen": {
        "first_name": "Yan",
        "last_name": "Chen",
        "department": "Computer Science",
        "overall_rating": 3.3,
        "quality": 3.3,
        "num_ratings": 53,
        "would_take_again": 61.0,
        "difficulty": 3.1,
        "tags": [
            "EXTRA CREDIT",
            "CLEAR GRADING CRITERIA",
            "LECTURE HEAVY",
            "CARING",
            "GROUP PROJECTS"
        ],
        "rating_distribution": {
            "5": 21,
            "4": 9,
            "3": 2,
            "2": 5,
            "1": 16
        },
        "courses": ["CS49J", "CS154", "CS166", "CS175"],
        "teaching_style": [
            "Recorded lectures available",
            "Optional attendance",
            "Heavy accent noted by students",
            "Reads from slides",
            "Generous extra credit (up to 30%)",
            "Group projects",
            "Weekly Canvas quizzes"
        ],
        "notes": [
            "Final can be replaced by project score",
            "Accent can be difficult to understand",
            "Self-study required",
            "Posts all materials on Canvas",
            "Quick email responses"
        ]
    },
    "amith_belman": {
        "first_name": "Amith",
        "last_name": "Belman",
        "department": "Computer Science",
        "overall_rating": 5.0,
        "quality": 5.0,
        "num_ratings": 6,
        "would_take_again": 100.0,
        "difficulty": 2.8,
        "tags": [
            "AMAZING LECTURES",
            "CLEAR GRADING CRITERIA",
            "GIVES GOOD FEEDBACK",
            "INSPIRATIONAL",
            "BEWARE OF POP QUIZZES"
        ],
        "rating_distribution": {
            "5": 6,
            "4": 0,
            "3": 0,
            "2": 0,
            "1": 0
        },
        "courses": ["CS156"],
        "teaching_style": [
            "Engaging lectures",
            "Weekly in-class quizzes",
            "Two exams per semester",
            "Detailed explanations",
            "Very accessible outside class",
            "Supportive in office hours"
        ],
        "notes": [
            "New professor at SJSU",
            "Specializes in AI",
            "Makes complex concepts approachable",
            "Interactive teaching style"
        ]
    },
    "sriram_rao": {
        "first_name": "Sriram",
        "last_name": "Rao",
        "department": "Computer Science",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 2,
        "would_take_again": 50.0,
        "difficulty": 4.5
    },
    "saptarshi_sengupta": {
        "first_name": "Saptarshi",
        "last_name": "Sengupta",
        "department": "Computer Science",
        "overall_rating": 4.5,
        "quality": 4.5,
        "num_ratings": 2,
        "would_take_again": 100.0,
        "difficulty": 3.5
    },
    "maryam_khazaei_pool": {
        "first_name": "Maryam",
        "last_name": "Khazaei Pool",
        "department": "Computer Science",
        "overall_rating": 3.0,
        "quality": 3.0,
        "num_ratings": 2,
        "would_take_again": 50.0,
        "difficulty": 2.5,
        "tags": [
            "TOUGH GRADER",
            "PARTICIPATION MATTERS",
            "AMAZING LECTURES",
            "CLEAR GRADING CRITERIA",
            "CARING"
        ],
        "rating_distribution": {
            "5": 1,
            "4": 0,
            "3": 0,
            "2": 0,
            "1": 1
        },
        "courses": ["CS146"],
        "teaching_style": [
            "Interactive lectures",
            "Group work during class",
            "In-class practice questions",
            "Mandatory attendance",
            "Emphasis on participation"
        ],
        "notes": [
            "Mixed reviews on grading fairness",
            "Provides comprehensive resources",
            "In-class work important for exams",
            "Helpful with clarifications",
            "New professor with limited ratings"
        ]
    },
    "sayma_akther": {
        "first_name": "Sayma",
        "last_name": "Akther", 
        "department": "Computer Science",
        "overall_rating": 2.9,
        "num_ratings": 20,
        "would_take_again": 45.0,
        "difficulty": 2.6,
        "tags": [
            "PARTICIPATION MATTERS",
            "CARING",
            "LECTURE HEAVY", 
            "CLEAR GRADING CRITERIA",
            "TOUGH GRADER"
        ],
        "rating_distribution": {
            "5": 5,
            "4": 0,
            "3": 6,
            "2": 5,
            "1": 4
        },
        "courses": ["CS46A", "CS156"],
        "teaching_style": [
            "Fast-paced lectures",
            "Mandatory attendance with roll-call",
            "In-class participation exercises",
            "Paper-based coding exams",
            "Limited homework assignments",
            "Group projects in CS156"
        ],
        "notes": [
            "New professor (started Fall 2023)",
            "Mixed reviews on teaching effectiveness",
            "Soft-spoken in lectures",
            "Punctuality issues reported",
            "Some exam questions beyond covered material",
            "Lenient grading with curves in CS156"
        ]
    },
    "wendy_lee": {
        "first_name": "Wendy",
        "last_name": "Lee",
        "department": "Computer Science",
        "overall_rating": 4.7,
        "num_ratings": 20,
        "would_take_again": 100.0,
        "difficulty": 2.9,
        "tags": [
            "CARING",
            "AMAZING LECTURES",
            "CLEAR GRADING CRITERIA",
            "GROUP PROJECTS",
            "LECTURE HEAVY"
        ],
        "rating_distribution": {
            "5": 13,
            "4": 7,
            "3": 0,
            "2": 0,
            "1": 0
        },
        "courses": ["CS22A", "CS46B", "CS122", "CS133"],
        "teaching_style": [
            "Interactive and engaging lectures",
            "Pop quizzes for attendance",
            "Hands-on assignments",
            "Group projects",
            "Online tutorials and resources",
            "Flexible with course adjustments",
            "Emphasis on practical applications"
        ],
        "notes": [
            "Very highly rated professor",
            "Accommodating during COVID transition",
            "Brings donuts and coffee to encourage attendance",
            "Strong focus on modern tools and libraries",
            "Concerned about AI/ChatGPT usage",
            "Exams use full time allocation"
        ]
    },
    "ethel_tshukudu": {
        "first_name": "Ethel",
        "last_name": "Tshukudu",
        "department": "Computer Science",
        "overall_rating": 5.0,
        "num_ratings": 3,
        "would_take_again": 100.0,
        "difficulty": 3.0,
        "tags": [
            "EXTRA CREDIT",
            "CARING",
            "GROUP PROJECTS",
            "GIVES GOOD FEEDBACK",
            "INSPIRATIONAL"
        ],
        "rating_distribution": {
            "5": 3,
            "4": 0,
            "3": 0,
            "2": 0,
            "1": 0
        },
        "courses": ["CS151"],
        "teaching_style": [
            "Well-organized slides",
            "Project-based learning",
            "No regular homework",
            "Clear exam preparation",
            "Group work emphasis",
            "Optional attendance",
            "Detailed feedback"
        ],
        "notes": [
            "New/young professor",
            "Very passionate about teaching",
            "Exams closely follow lectures",
            "Quick response to students",
            "Relates well to students",
            "Strong focus on student success"
        ]
    },
    "kevin_smith": {
        "first_name": "Kevin",
        "last_name": "Smith",
        "department": "Computer Science",
        "overall_rating": 4.2,
        "num_ratings": 13,
        "would_take_again": 77.0,
        "difficulty": 3.2,
        "tags": [
            "ACCESSIBLE OUTSIDE CLASS",
            "GIVES GOOD FEEDBACK",
            "LOTS OF HOMEWORK",
            "CARING",
            "GROUP PROJECTS"
        ],
        "rating_distribution": {
            "5": 7,
            "4": 3,
            "3": 2,
            "2": 0,
            "1": 1
        },
        "courses": ["CS134", "CS116A", "CS116B", "CS235"],
        "teaching_style": [
            "Project-based learning",
            "Take-home assignments",
            "Industry experience integration",
            "Hands-on programming focus",
            "Optional attendance",
            "Lenient grading",
            "Provides starter code"
        ],
        "notes": [
            "Strong game industry background",
            "C++ heavy coursework",
            "Requires basic calculus and physics",
            "Quick email responses",
            "Helpful in office hours",
            "Some course organization issues noted"
        ]
    },
    "mike_wood": {
        "first_name": "Mike",
        "last_name": "Wood",
        "department": "Computer Science",
        "overall_rating": 5.0,
        "num_ratings": 8,
        "would_take_again": 100.0,
        "difficulty": 2.3,
        "tags": [
            "AMAZING LECTURES",
            "PARTICIPATION MATTERS",
            "EXTRA CREDIT",
            "LOTS OF HOMEWORK",
            "CARING"
        ],
        "rating_distribution": {
            "5": 8,
            "4": 0,
            "3": 0,
            "2": 0,
            "1": 0
        },
        "courses": ["CS46A", "CS122"],
        "teaching_style": [
            "Clear, engaging lectures",
            "Lots of examples",
            "Hybrid class format",
            "Open note exams",
            "Practice tests provided",
            "Weekly homework and labs",
            "Participation assignments"
        ],
        "notes": [
            "Perfect rating from all students",
            "Fast email responses",
            "Generous extra credit",
            "Clear grading criteria",
            "Canvas regularly updated",
            "Challenging but manageable workload",
            "Very patient with questions"
        ]
    },
    "nada_attar": {
        "first_name": "Nada",
        "last_name": "Attar",
        "department": "Computer Science",
        "overall_rating": 2.4,
        "num_ratings": 39,
        "would_take_again": 34.0,
        "difficulty": 3.4,
        "tags": [
            "TOUGH GRADER",
            "GRADED BY FEW THINGS",
            "CARING",
            "LECTURE HEAVY",
            "TEST HEAVY"
        ],
        "rating_distribution": {
            "5": 9,
            "4": 0,
            "3": 5,
            "2": 7,
            "1": 18
        },
        "courses": ["CS146", "CS22A"],
        "teaching_style": [
            "Theory-focused lectures",
            "Mandatory attendance",
            "Difficult homework",
            "Heavy emphasis on exams",
            "Slides-based teaching",
            "Office hours available",
            "Asynchronous options"
        ],
        "notes": [
            "Mixed reviews on teaching effectiveness",
            "Slow grading turnaround",
            "Confusing problem descriptions",
            "Limited coding practice",
            "Curves exams when needed",
            "Inconsistent email responses"
        ],
        "contact": {
            "email": "nada.attar@sjsu.edu",
            "office": "MQH 229",
            "office_hours": "Mon/Wed 3:00-4:00pm",
            "phone": "(408) 924-5156"
        },
        "academic": {
            "title": "Assistant Professor",
            "research_interests": ["Data Science", "Machine Learning", "CS Education"],
            "current_courses": ["CS146", "CS22A", "CS235"]
        },
    },
    "robert_chun": {
        "first_name": "Robert",
        "last_name": "Chun",
        "department": "Computer Science",
        "overall_rating": 4.2,
        "num_ratings": 48,
        "would_take_again": 60.0,
        "difficulty": 3.0,
        "tags": [
            "AMAZING LECTURES",
            "RESPECTED",
            "CARING",
            "TOUGH GRADER",
            "WOULD TAKE AGAIN"
        ],
        "rating_distribution": {
            "5": 33,
            "4": 7,
            "3": 2,
            "2": 3,
            "1": 3
        },
        "courses": ["CS147", "CS149", "CS159", "CS247", "CS259"],
        "teaching_style": [
            "Organized lecture notes",
            "Clear presentations",
            "Pre-recorded lectures available",
            "Student presentations component",
            "Limited assignments",
            "Test-focused assessment",
            "No textbook required"
        ],
        "notes": [
            "Mixed reviews on grading fairness",
            "Reuses course materials",
            "Strong focus on lecture notes",
            "Long but comprehensive exams",
            "Calm teaching style",
            "Same material for grad/undergrad courses",
            "Email response issues noted"
        ]
    },
    "melody_moh": {
        "first_name": "Melody",
        "last_name": "Moh",
        "department": "Computer Science",
        "overall_rating": 3.2,
        "num_ratings": 17,
        "would_take_again": 0.0,
        "difficulty": 3.2,
        "tags": [
            "TOUGH GRADER",
            "LOTS OF HOMEWORK",
            "SO MANY PAPERS",
            "LECTURE HEAVY",
            "TEST HEAVY"
        ],
        "rating_distribution": {
            "5": 5,
            "4": 3,
            "3": 5,
            "2": 1,
            "1": 3
        },
        "courses": ["CS158A", "CS158B", "CS258"],
        "teaching_style": [
            "Project-heavy coursework",
            "Detailed networking focus",
            "Mandatory attendance",
            "Difficult exams",
            "Heavy workload",
            "Curved grading",
            "Team projects"
        ],
        "notes": [
            "Current department chair",
            "Slow grading turnaround",
            "Poor email response rate",
            "Strong networking knowledge",
            "Significant grade curves",
            "Communication issues noted",
            "Mixed reviews on organization"
        ]
    },
    "chris_pollett": {
        "first_name": "Chris",
        "last_name": "Pollett",
        "department": "Computer Science",
        "overall_rating": 3.3,
        "num_ratings": 64,
        "would_take_again": 53.0,
        "difficulty": 3.7,
        "tags": [
            "GET READY TO READ",
            "TOUGH GRADER",
            "EXTRA CREDIT",
            "LOTS OF HOMEWORK",
            "CLEAR GRADING CRITERIA"
        ],
        "rating_distribution": {
            "5": 18,
            "4": 18,
            "3": 12,
            "2": 6,
            "1": 10
        },
        "courses": ["CS152", "CS154", "CS156", "CS157A", "CS157B", "CS158A", "CS174", "CS256", "CS257", "CS267"],
        "teaching_style": [
            "Dense lecture slides",
            "Weekly quizzes",
            "In-class activities",
            "Heavy memorization focus",
            "Group work allowed",
            "Recorded lectures available",
            "Significant safety nets"
        ],
        "notes": [
            "Mixed reviews on teaching effectiveness",
            "Generous curves noted",
            "Reuses exam questions",
            "Heavy workload in assignments",
            "Strong theoretical focus",
            "Accessible in office hours",
            "Passing grade at 55%"
        ]
    }
} 

def format_professor_info(professor):
    """Format professor information into a readable string"""
    def get_rating_color(rating):
        try:
            rating = float(rating)
            if rating >= 4.0: return "#28a745"  # Good - Green
            if rating >= 3.0: return "#ffc107"  # Average - Yellow
            return "#dc3545"  # Poor - Red
        except:
            return "#6c757d"  # Default - Gray
    
    def get_would_take_again_color(percent):
        try:
            percent = float(percent)
            if percent >= 70: return "#28a745"
            if percent >= 40: return "#ffc107"
            return "#dc3545"
        except:
            return "#6c757d"
    
    # Start with basic info that's always present
    info = [
        f"<div style='font-size: 1.2em; font-weight: bold; margin-bottom: 8px;'>👨‍🏫 {professor['first_name']} {professor['last_name']}</div>",
        # Academic title if available
        *(
            [f"<div style='color: var(--dark-blue); font-weight: 500;'>{professor['academic']['title']}</div>"]
            if 'academic' in professor and 'title' in professor['academic']
            else []
        ),
        f"<div>🏛️ <span style='font-weight: 500;'>Department:</span> {professor['department']}</div>",
        
        # Contact Information
        *(
            [
                f"<div style='margin-top: 12px;'><span style='font-weight: 500;'>📧 Contact Information:</span></div>",
                "<div style='margin-left: 12px; line-height: 1.5;'>"
            ] +
            [f"<div>• Email: <a href='mailto:{professor['contact']['email']}'>{professor['contact']['email']}</a></div>" if 'email' in professor['contact'] else ""] +
            [f"<div>• Office: {professor['contact']['office']}</div>" if 'office' in professor['contact'] else ""] +
            [f"<div>• Office Hours: {professor['contact']['office_hours']}</div>" if 'office_hours' in professor['contact'] else ""] +
            [f"<div>• Phone: {professor['contact']['phone']}</div>" if 'phone' in professor['contact'] else ""] +
            [f"<div>• Website: <a href='{professor['contact']['website']}' target='_blank'>{professor['contact']['website']}</a></div>" if 'website' in professor['contact'] else ""] +
            [f"<div>• Zoom: <a href='{professor['contact']['zoom_link']}' target='_blank'>Join Zoom Meeting</a></div>" if 'zoom_link' in professor['contact'] else ""] +
            ["</div>"]
            if 'contact' in professor else []
        ),
        
        # Academic Information
        *(
            [
                f"<div style='margin-top: 12px;'><span style='font-weight: 500;'>🎓 Academic Background:</span></div>",
                "<div style='margin-left: 12px; line-height: 1.5;'>"
            ] +
            [f"<div style='margin-bottom: 8px;'><strong>Research Interests:</strong><br>" + 
             "<ul style='margin: 4px 0 8px 20px;'>" +
             "".join([f"<li>{interest}</li>" for interest in professor['academic']['research_interests']]) +
             "</ul></div>" if 'research_interests' in professor['academic'] else ""] +
            [f"<div style='margin-bottom: 8px;'><strong>Education:</strong><br>" +
             "<ul style='margin: 4px 0 8px 20px;'>" +
             "".join([f"<li>{degree}</li>" for degree in professor['academic']['education']]) +
             "</ul></div>" if 'education' in professor['academic'] else ""] +
            [f"<div><strong>Current Courses:</strong> {', '.join(professor['academic']['current_courses'])}</div>" if 'current_courses' in professor['academic'] else ""] +
            ["</div>"]
            if 'academic' in professor else []
        ),
        
        f"<div style='color: {get_rating_color(professor['overall_rating'])}; font-weight: 500;'>⭐ Overall Rating: {professor['overall_rating']}/5.0</div>",
        f"<div>📊 <span style='font-weight: 500;'>Based on</span> {professor['num_ratings']} ratings</div>",
        f"<div style='color: {get_would_take_again_color(professor['would_take_again'])}; font-weight: 500;'>👍 Would Take Again: {professor['would_take_again']}%</div>",
        f"<div>📚 <span style='font-weight: 500;'>Difficulty:</span> {professor['difficulty']}/5.0</div>"
    ]
    
    # Add optional sections only if they exist and are not empty
    if 'tags' in professor and professor['tags']:
        tags_html = "\n<div style='margin-top: 12px;'><span style='font-weight: 500;'>🏷️ Common Tags:</span></div><div>" + " ".join([
            f"<span class='tag'>{tag}</span>" 
            for tag in professor['tags']
        ]) + "</div>"
        info.append(tags_html)
    
    if 'courses' in professor and professor['courses']:
        courses_html = "\n<div style='margin-top: 12px;'><span style='font-weight: 500;'>📚 Courses:</span></div><div>" + " ".join([
            f"<span class='course-tag'>{course}</span>" 
            for course in professor['courses']
        ]) + "</div>"
        info.append(courses_html)
    
    if 'teaching_style' in professor and professor['teaching_style']:
        info.append("\n<div style='margin-top: 12px;'><span style='font-weight: 500;'>📝 Teaching Style:</span></div>")
        info.append("<div style='margin-left: 12px;'>")
        info.extend([f"<div style='margin: 4px 0;'>• {style}</div>" for style in professor['teaching_style']])
        info.append("</div>")
    
    if 'notes' in professor and professor['notes']:
        info.append("\n<div style='margin-top: 12px;'><span style='font-weight: 500;'>📌 Additional Notes:</span></div>")
        info.append("<div style='margin-left: 12px;'>")
        info.extend([f"<div style='margin: 4px 0;'>• {note}</div>" for note in professor['notes']])
        info.append("</div>")
    
    return "\n".join(info)

def get_professors_by_course(course_code):
    """
    Returns a list of professors who teach a specific course.
    Args:
        course_code (str): The course code to search for (e.g. 'CS146' or 'CS 146')
    Returns:
        str: Formatted string with professors who teach the course
    """
    # Normalize course code by removing spaces
    normalized_code = course_code.replace(" ", "").upper()
    
    matching_professors = []
    for prof_id, prof_data in SJSU_PROFESSORS.items():
        if "courses" in prof_data:
            # Normalize stored courses for comparison
            normalized_courses = [c.replace(" ", "").upper() for c in prof_data["courses"]]
            if normalized_code in normalized_courses:
                matching_professors.append(prof_data)
    
    if matching_professors:
        result = f"Professors who teach {course_code}:\n"
        for prof in matching_professors:
            result += f"- {format_professor_info(prof)}\n"
        return result
    return f"No professors found who teach {course_code}"

def search_professors(query):
    """
    Search for professors based on various criteria
    Returns:
        str: Formatted response with search results
    """
    # Check if query is asking about who teaches a course
    query_lower = query.lower()
    if ("teach" in query_lower or "who" in query_lower) and "cs" in query_lower:
        # Extract course number
        import re
        course_match = re.search(r'cs\s*(\d+\w*)', query.lower())
        if course_match:
            course_code = f"CS{course_match.group(1)}"
            return get_professors_by_course(course_code)
    return "I couldn't understand your query. Try asking something like 'Who teaches CS146?'"

# Make the functions available at module level
__all__ = ['SJSU_PROFESSORS', 'get_professors_by_course', 'search_professors']