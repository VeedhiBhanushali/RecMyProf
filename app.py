from tools.ratemyprof_api.sjsu_professors import SJSU_PROFESSORS, search_professors

async def handle_message(websocket, message):
    # For professor name queries
    for prof_id, prof_data in SJSU_PROFESSORS.items():
        if message.lower() in f"{prof_data['first_name']} {prof_data['last_name']}".lower():
            response = f"""Professor Information:
  - Name: {prof_data['first_name']} {prof_data['last_name']}
  - Department: {prof_data['department']}
  - Overall Rating: {prof_data['overall_rating']}/5.0
  - Number of Ratings: {prof_data['num_ratings']}
  - Would Take Again: {prof_data['would_take_again']}%
  - Difficulty: {prof_data['difficulty']}/5.0
  - Tags: {', '.join(prof_data['tags'])}
  - Courses: {', '.join(prof_data['courses'])}
  
  Teaching Style:
  {chr(10).join('- ' + style for style in prof_data['teaching_style'])}
  
  Notes:
  {chr(10).join('- ' + note for note in prof_data['notes'])}"""
            await websocket.send(response)
            return

    # For course queries
    if ("teach" in message.lower() or "who" in message.lower()) and "cs" in message.lower():
        response = search_professors(message)
        await websocket.send(response)
        return 