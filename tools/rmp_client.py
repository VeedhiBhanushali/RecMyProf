import os
import sys
from typing import Optional, Dict

# Get the absolute path to the tools directory
tools_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(tools_dir)

# Add both directories to Python path
for path in [tools_dir, parent_dir]:
    if path not in sys.path:
        sys.path.append(path)

from .ratemyprof_api.ratemyprof_api import RateMyProfApi

class RMPClient:
    def __init__(self):
        self._school_cache: Dict[str, RateMyProfApi] = {}
        # School IDs from RMP (verified working IDs)
        self.school_ids = {
            "SJSU": "1074",    # San Jose State University
            "UCI": "1076",     # UC Irvine (fixed ID)
            "MIT": "580",      # Massachusetts Institute of Technology
            "Stanford": "953",  # Stanford University
            "Harvard": "399",   # Harvard University
            "Berkeley": "1072", # UC Berkeley
            "UCLA": "1075",    # UC Los Angeles
            "UCSD": "1079",    # UC San Diego
            "USC": "1381"      # University of Southern California
        }
    
    def _get_school_api(self, school_name: str) -> Optional[RateMyProfApi]:
        """Get or create RateMyProfApi instance for a school"""
        school_id = self.school_ids.get(school_name.upper())
        if not school_id:
            print(f"School {school_name} not found in school IDs")
            return None
            
        if school_id not in self._school_cache:
            try:
                api = RateMyProfApi(school_id)
                # Test the API by accessing professors
                _ = api.professors
                self._school_cache[school_id] = api
            except Exception as e:
                print(f"Error initializing API for school {school_name}: {e}")
                return None
                
        return self._school_cache[school_id]
    
    def search_professor(self, name: str, school: str = "SJSU") -> Optional[dict]:
        """Search for a professor by name at a specific school"""
        try:
            print(f"Searching for '{name}' at '{school}'")  # Debug print
            api = self._get_school_api(school)
            if not api:
                return None
                
            professors = api.professors
            if not professors:
                print(f"No professors found at {school}")
                return None
            
            # Search through professors
            name_lower = name.lower().strip()
            name_parts = name_lower.split()
            
            # Try exact match first
            for prof_id, professor in professors.items():
                full_name = f"{professor.first_name} {professor.last_name}".lower()
                if name_lower == full_name:
                    print(f"Found exact match: {professor.first_name} {professor.last_name}")
                    return self._format_professor(professor, school)
            
            # Try partial match
            for prof_id, professor in professors.items():
                full_name = f"{professor.first_name} {professor.last_name}".lower()
                # Check if all parts of the search name are in the professor's name
                if all(part in full_name for part in name_parts):
                    print(f"Found partial match: {professor.first_name} {professor.last_name}")
                    return self._format_professor(professor, school)
            
            print(f"Professor '{name}' not found at {school}")
            return None
            
        except Exception as e:
            print(f"Error searching for professor: {e}")
            return None
            
    def _format_professor(self, professor, school: str) -> dict:
        """Format professor data into a consistent dictionary"""
        return {
            "name": f"{professor.first_name} {professor.last_name}",
            "department": getattr(professor, 'department', 'Not specified'),
            "school": school,
            "rating": {
                "overall": float(professor.overall_rating) if professor.overall_rating != "N/A" else None,
                "total_ratings": professor.num_ratings,
                "would_take_again": getattr(professor, 'would_take_again', 'N/A'),
                "difficulty": getattr(professor, 'difficulty', 'N/A')
            }
        }

    def get_professor_info(self, professor_name):
        try:
            # Query Pinecone for professor info
            results = self.index.query(
                vector=get_embedding(professor_name),
                top_k=1,
                namespace="sjsu",
                include_metadata=True
            )
            
            if results.matches:
                metadata = results.matches[0].metadata
                # Include contact info and research in the response
                if "contact_info" in SJSU_PROFESSORS:
                    prof_id = results.matches[0].id.replace("sjsu_prof_", "")
                    if prof_id in SJSU_PROFESSORS["contact_info"]:
                        metadata.update(SJSU_PROFESSORS["contact_info"][prof_id])
                return metadata
            return None
        except Exception as e:
            print(f"Error in get_professor_info: {e}")
            return None 