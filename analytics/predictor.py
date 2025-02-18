from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
from tools.ratemyprof_api.sjsu_professors import SJSU_PROFESSORS

class ProfessorPredictor:
    def __init__(self):
        self.df = pd.DataFrame.from_dict(SJSU_PROFESSORS, orient='index')
        self.label_encoder = LabelEncoder()
        self.model = RandomForestRegressor(n_estimators=100)
        self._prepare_data()
        
    def _prepare_data(self):
        """Prepare data for modeling"""
        # Encode categorical variables
        self.df['department_encoded'] = self.label_encoder.fit_transform(self.df['department'])
        
        # Create feature matrix
        self.features = ['department_encoded', 'difficulty']
        self.target = 'overall_rating'
        
        # Split data
        X = self.df[self.features]
        y = self.df[self.target]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2)
        
        # Train model
        self.model.fit(self.X_train, self.y_train)
    
    def predict_success(self, student_context, professor_data):
        """Predict student success likelihood with a professor"""
        # Convert professor data to features
        prof_features = np.array([
            self.label_encoder.transform([professor_data['department']])[0],
            professor_data['difficulty']
        ]).reshape(1, -1)
        
        # Get base prediction
        base_score = self.model.predict(prof_features)[0]
        
        # Adjust based on student context
        context_adjustments = {
            'international': -0.2 if professor_data.get('esl_friendly', False) else 0,
            'working': -0.3 if professor_data.get('strict_attendance', True) else 0,
            'first_gen': 0.2 if professor_data.get('supportive', True) else 0,
            'evening_preference': 0.3 if professor_data.get('evening_classes', False) else 0
        }
        
        # Apply adjustments
        final_score = base_score
        for context, adjustment in context_adjustments.items():
            if student_context.get(context):
                final_score += adjustment
                
        return max(min(final_score, 5.0), 1.0)  # Ensure score is between 1 and 5 