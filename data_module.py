from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Add this to prevent GUI backend errors
import io
import base64
from tools.ratemyprof_api.sjsu_professors import SJSU_PROFESSORS

data_module = Blueprint('data_module', __name__, template_folder='templates')

def generate_professor_stats():
    try:
        # Convert SJSU_PROFESSORS dictionary to DataFrame
        df = pd.DataFrame.from_dict(SJSU_PROFESSORS, orient='index')
        
        # Generate department-specific analytics
        dept_analytics = {}
        for dept in df['department'].unique():
            dept_data = df[df['department'] == dept]
            dept_analytics[dept] = {
                'count': len(dept_data),
                'avg_rating': dept_data['overall_rating'].mean(),
                'avg_difficulty': dept_data['difficulty'].mean(),
                'would_take_again': dept_data['would_take_again'].mean(),
                'top_tags': get_top_tags(dept_data),
                'rating_trend': calculate_rating_trend(dept_data),
                'student_success': calculate_student_success(dept_data),
                'top_professors': get_top_professors(dept_data),
                'rating_distribution': create_dept_rating_dist(dept_data),
                'teaching_metrics': analyze_teaching_metrics(dept_data)
            }
        
        # Generate statistics
        stats = {
            'avg_rating': df['overall_rating'].mean(),
            'avg_difficulty': df['difficulty'].mean(),
            'total_professors': len(df),
            'avg_would_take_again': df['would_take_again'].mean(),
            'departments': dept_analytics
        }
        
        # Generate rating distribution plot
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='overall_rating', bins=20)
        plt.title('Distribution of Professor Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        
        # Convert plot to base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close()
        
        return stats, plot_url
    except Exception as e:
        print(f"Error generating stats: {e}")
        return {}, ''

def get_top_tags(dept_data):
    """Get most common tags for a department"""
    all_tags = []
    for tags in dept_data['tags']:
        all_tags.extend(tags)
    tag_counts = pd.Series(all_tags).value_counts()
    return tag_counts.head(5).to_dict()

def calculate_rating_trend(dept_data):
    """Calculate rating trends"""
    return {
        'improving': len(dept_data[dept_data['overall_rating'] >= 4.0]),
        'stable': len(dept_data[(dept_data['overall_rating'] >= 3.0) & (dept_data['overall_rating'] < 4.0)]),
        'needs_improvement': len(dept_data[dept_data['overall_rating'] < 3.0])
    }

def calculate_student_success(dept_data):
    """Calculate student success metrics"""
    return {
        'high_success': len(dept_data[dept_data['would_take_again'] >= 80]),
        'medium_success': len(dept_data[(dept_data['would_take_again'] >= 50) & (dept_data['would_take_again'] < 80)]),
        'low_success': len(dept_data[dept_data['would_take_again'] < 50])
    }

def get_top_professors(dept_data, n=5):
    """Get top performing professors in department"""
    top_profs = dept_data.nlargest(n, 'overall_rating')
    return [{
        'name': f"{row['first_name']} {row['last_name']}",
        'rating': row['overall_rating'],
        'would_take_again': row['would_take_again'],
        'top_course': get_best_course(row['courses']),
        'strength': get_professor_strength(row)
    } for _, row in top_profs.iterrows()]

def get_best_course(courses):
    """Get the most frequently taught course"""
    return courses[0] if courses else "N/A"

def get_professor_strength(prof_data):
    """Determine professor's key strength"""
    strengths = {
        'Clear Lecturer': prof_data['tags'].count('CLEAR GRADING'),
        'Engaging': prof_data['tags'].count('ENGAGING'),
        'Helpful': prof_data['tags'].count('CARING'),
        'Fair': prof_data['tags'].count('RESPECTED')
    }
    return max(strengths.items(), key=lambda x: x[1])[0]

def create_dept_rating_dist(dept_data):
    """Create rating distribution for department"""
    ratings = pd.cut(dept_data['overall_rating'], 
                    bins=[0, 2, 3, 4, 5], 
                    labels=['Poor', 'Fair', 'Good', 'Excellent'])
    return ratings.value_counts().to_dict()

def analyze_teaching_metrics(dept_data):
    """Analyze detailed teaching metrics"""
    return {
        'engagement': {
            'high': len(dept_data[dept_data['tags'].apply(lambda x: 'ENGAGING' in x)]),
            'medium': len(dept_data[dept_data['tags'].apply(lambda x: 'LECTURE HEAVY' in x)]),
            'low': len(dept_data[dept_data['tags'].apply(lambda x: 'BORING' in x)])
        },
        'workload': {
            'heavy': len(dept_data[dept_data['tags'].apply(lambda x: 'TOUGH GRADER' in x)]),
            'moderate': len(dept_data[dept_data['tags'].apply(lambda x: 'CLEAR GRADING' in x)]),
            'light': len(dept_data[dept_data['tags'].apply(lambda x: 'GIVES GOOD FEEDBACK' in x)])
        }
    }

@data_module.route('/pref', methods=['GET', 'POST'])
def preferences():
    print("Preferences route accessed")  # Debug print
    if request.method == 'POST':
        try:
            preferences = {
                'teaching_style': request.form.get('teaching_style'),
                'min_rating': float(request.form.get('min_rating', 0) or 0),
                'max_difficulty': float(request.form.get('max_difficulty', 5) or 5),
                'department': request.form.get('department'),
                'would_take_again': float(request.form.get('would_take_again', 0) or 0)
            }
            
            # Filter professors based on preferences
            matching_professors = filter_professors(preferences)
            return jsonify({'professors': matching_professors})
        except ValueError as e:
            return jsonify({'error': 'Invalid input values. Please check your inputs.'}), 400
        except Exception as e:
            return jsonify({'error': 'An error occurred processing your request.'}), 500
        
    return render_template('preferences.html')

@data_module.route('/dash')
def dashboard():
    print("Dashboard route accessed")  # Debug print
    stats, plot_url = generate_professor_stats()
    return render_template('dashboard.html', stats=stats, plot_url=plot_url)

def filter_professors(preferences):
    matching = []
    for prof_id, prof in SJSU_PROFESSORS.items():
        try:
            if (prof['overall_rating'] >= preferences['min_rating'] and
                prof['difficulty'] <= preferences['max_difficulty'] and
                prof['would_take_again'] >= preferences['would_take_again'] and
                (not preferences['department'] or prof['department'] == preferences['department'])):
                matching.append(prof)
        except (KeyError, TypeError) as e:
            print(f"Error processing professor {prof_id}: {e}")
            continue
    return matching 