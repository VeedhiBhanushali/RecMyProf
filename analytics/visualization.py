import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from collections import Counter
from tools.ratemyprof_api.sjsu_professors import SJSU_PROFESSORS

class ProfessorAnalytics:
    def __init__(self):
        self.df = pd.DataFrame.from_dict(SJSU_PROFESSORS, orient='index')
        self._process_feedback()
    
    def _process_feedback(self):
        """Process and categorize student feedback"""
        # Sentiment categories
        self.sentiment_categories = {
            'Positive': ['amazing', 'great', 'excellent', 'good', 'helpful', 'clear', 'caring'],
            'Neutral': ['okay', 'fair', 'average', 'decent', 'moderate'],
            'Negative': ['difficult', 'tough', 'hard', 'confusing', 'unclear']
        }

        # Teaching aspects
        self.teaching_aspects = {
            'Communication': ['clear', 'explains', 'communication', 'lectures'],
            'Workload': ['assignments', 'homework', 'projects', 'workload'],
            'Engagement': ['engaging', 'interesting', 'interactive', 'boring'],
            'Support': ['helpful', 'office hours', 'available', 'supportive'],
            'Grading': ['fair', 'grading', 'tests', 'exams', 'quizzes']
        }
    
    def create_rating_distribution(self):
        """Create interactive rating distribution visualization"""
        fig = px.histogram(
            self.df, 
            x="overall_rating",
            nbins=20,
            title="Professor Rating Distribution",
            labels={"overall_rating": "Rating", "count": "Number of Professors"},
            color_discrete_sequence=['#0055A2']  # SJSU Blue
        )
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font={'family': 'Inter'}
        )
        return fig.to_html(full_html=False)
    
    def create_department_comparison(self):
        """Create department comparison visualization"""
        dept_stats = self.df.groupby('department').agg({
            'overall_rating': 'mean',
            'difficulty': 'mean',
            'would_take_again': 'mean'
        }).round(2)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Rating',
            x=dept_stats.index,
            y=dept_stats.overall_rating,
            marker_color='#0055A2'  # SJSU Blue
        ))
        
        fig.add_trace(go.Bar(
            name='Difficulty',
            x=dept_stats.index,
            y=dept_stats.difficulty,
            marker_color='#B8A364'  # SJSU Gold
        ))
        
        fig.update_layout(
            title="Department Performance Comparison",
            barmode='group',
            plot_bgcolor='white',
            paper_bgcolor='white',
            font={'family': 'Inter'}
        )
        
        return fig.to_html(full_html=False)
    
    def create_correlation_matrix(self):
        """Create correlation matrix of professor metrics"""
        corr_matrix = self.df[['overall_rating', 'difficulty', 'would_take_again']].corr()
        
        fig = px.imshow(
            corr_matrix,
            labels=dict(color="Correlation"),
            title="Correlation between Teaching Metrics",
            color_continuous_scale=[[0, '#B8A364'], [0.5, 'white'], [1, '#0055A2']]  # SJSU colors
        )
        
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font={'family': 'Inter'}
        )
        
        return fig.to_html(full_html=False)
    
    def create_feedback_analysis(self):
        """Create student feedback visualization"""
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                "Feedback Sentiment Distribution",
                "Teaching Aspects Mentioned",
                "Common Feedback Themes",
                "Feedback Over Time"
            ),
            specs=[[{"type": "pie"}, {"type": "bar"}],
                  [{"type": "bar"}, {"type": "scatter"}]]
        )

        # 1. Sentiment Distribution (Pie Chart)
        sentiment_counts = self._analyze_sentiment()
        fig.add_trace(
            go.Pie(
                labels=list(sentiment_counts.keys()),
                values=list(sentiment_counts.values()),
                marker_colors=['#4CAF50', '#FFC107', '#F44336'],
                hole=0.3
            ),
            row=1, col=1
        )

        # 2. Teaching Aspects (Bar Chart)
        aspects_data = self._analyze_teaching_aspects()
        fig.add_trace(
            go.Bar(
                x=list(aspects_data.keys()),
                y=list(aspects_data.values()),
                marker_color='#0055A2'
            ),
            row=1, col=2
        )

        # 3. Common Themes (Word Cloud Bar Chart)
        themes_data = self._analyze_common_themes()
        fig.add_trace(
            go.Bar(
                x=list(themes_data.keys()),
                y=list(themes_data.values()),
                marker_color='#B8A364'
            ),
            row=2, col=1
        )

        # 4. Feedback Trends
        trend_data = self._analyze_feedback_trends()
        fig.add_trace(
            go.Scatter(
                x=list(trend_data.keys()),
                y=list(trend_data.values()),
                mode='lines+markers',
                line=dict(color='#0055A2')
            ),
            row=2, col=2
        )

        # Update layout
        fig.update_layout(
            height=800,
            showlegend=False,
            title_text="Student Feedback Analysis",
            plot_bgcolor='white',
            paper_bgcolor='white',
            font={'family': 'Inter'}
        )

        return fig.to_html(full_html=False)

    def _analyze_sentiment(self):
        """Analyze sentiment distribution in feedback"""
        sentiment_counts = {'Positive': 0, 'Neutral': 0, 'Negative': 0}
        
        for _, row in self.df.iterrows():
            if not isinstance(row.get('tags', []), list):
                continue
            
            tags = ' '.join(row['tags']).lower()
            
            # Count occurrences of sentiment words
            for sentiment, words in self.sentiment_categories.items():
                if any(word in tags for word in words):
                    sentiment_counts[sentiment] += 1
        
        return sentiment_counts

    def _analyze_teaching_aspects(self):
        """Analyze mentioned teaching aspects"""
        aspect_counts = {aspect: 0 for aspect in self.teaching_aspects.keys()}
        
        for _, row in self.df.iterrows():
            if not isinstance(row.get('tags', []), list):
                continue
            
            tags = ' '.join(row['tags']).lower()
            
            for aspect, keywords in self.teaching_aspects.items():
                if any(keyword in tags for keyword in keywords):
                    aspect_counts[aspect] += 1
        
        return aspect_counts

    def _analyze_common_themes(self):
        """Analyze common themes in feedback"""
        all_tags = []
        for _, row in self.df.iterrows():
            if isinstance(row.get('tags', []), list):
                all_tags.extend(row['tags'])
        
        # Get top 10 most common themes
        return dict(Counter(all_tags).most_common(10))

    def _analyze_feedback_trends(self):
        """Analyze feedback trends over time"""
        # Simulate trend data (replace with actual data if available)
        return {
            'Spring 2023': 4.2,
            'Summer 2023': 4.3,
            'Fall 2023': 4.1,
            'Winter 2024': 4.4,
            'Spring 2024': 4.3
        } 