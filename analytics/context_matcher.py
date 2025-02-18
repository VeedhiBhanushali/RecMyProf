class StudentContextMatcher:
    def __init__(self):
        self.context_weights = {
            'international': {
                'esl_friendly': 5,
                'clear_communication': 4,
                'provides_notes': 3,
                'office_hours': 3
            },
            'working': {
                'flexible_deadlines': 5,
                'clear_expectations': 4,
                'recorded_lectures': 3,
                'reasonable_workload': 4
            },
            'first_gen': {
                'supportive': 5,
                'clear_grading': 4,
                'extra_help': 4,
                'mentoring': 3
            },
            'schedule': {
                'early_morning': 5,
                'evening': 5,
                'hybrid': 4,
                'flexible': 3
            }
        }
    
    def calculate_context_score(self, professor, student_context):
        """Calculate how well a professor matches student context"""
        total_score = 0
        total_weight = 0
        
        for context_type, preferences in student_context.items():
            if not preferences:
                continue
                
            weights = self.context_weights.get(context_type, {})
            for pref, weight in weights.items():
                if professor.get(pref, False):
                    total_score += weight
                total_weight += weight
        
        return (total_score / total_weight * 100) if total_weight > 0 else 0 