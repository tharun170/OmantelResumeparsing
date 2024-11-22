from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import time


app = Flask(__name__)
CORS(app)


 
jd1 = {
    "id": "data-engineer-001",
    "title": "Data Engineer",
    "company": "Omantel",
    "description": {
        "overview": "We are seeking a talented data professional as a Data Engineer to join our Data Engineering team. This role requires a strong focus and experience in software development, multi-cloud based technologies, in memory data stores, and a strong desire to learn complex systems and new technologies.",
        "responsibilities": [
            "Design, develop, write, and modify code",
            "Design, develop, maintain code, and support for web-based applications and ETLs using Python Fastapi",
            "Support multi-cloud application development",
            "Design and build complex systems that can scale rapidly",
            "Design and implement effective service/product interfaces",
            "Contribute to technical standards",
            "Support development stages for application development",
            "Influence company wide engineering standards",
            "Conduct code reviews and develop documentation"
        ],
        "requirements": [
            "Bachelor's degree in computer science, IT, or related field",
            "1+ years of experience programming, building & supporting SaaS web applications",
            "1+ years of experience programming in Python Fastapi",
            "1+ years of experience with ETL workflow implementation",
            "Knowledge of database architecture",
            "Strong communication and collaboration skills"
        ],
        "skills": [
            "Python",
            "FastAPI",
            "ETL",
            "AWS",
            "GCP",
            "SQL",
            "Github",
            "Jenkins"
        ]
    }
}

jd2 = {
    "id": "senior-manager-growth-001",
    "title": "Senior Manager, Growth Portfolio",
    "company": "Omantel",
    "description": {
        "overview": "To develop and implement strategies to monetize data assets effectively, while also identifying and capitalizing on growth opportunities within specific customer segments.",
        "position_info": {
            "unit": "Business Unit",
            "division": "Growth Portfolio",
            "location": "HQ",
            "grade": "L2",
            "experience_required": "8-15 years"
        },
        "responsibilities": [
            "Develop and refine strategies to identify high-value customer segments",
            "Implement initiatives to monetize data assets",
            "Drive revenue growth through targeted strategies",
            "Cultivate strategic partnerships",
            "Establish KPIs and metrics",
            "Maintain deep knowledge of big data and analytics",
            "Work closely with product management and marketing",
            "Ensure alignment with company ethics",
            "Build a results-driven team culture"
        ],
        "requirements": [
            "Bachelor in relevant field",
            "8 years of total experience",
            "3 years in a managerial position"
        ],
        "competencies": {
            "leadership": [
                "Assertiveness and Conflict Resolution",
                "Fostering Learning and Development",
                "Inspiring and Leading Others",
                "Leading Change and Cultivates Innovation",
                "Visioning and Alignment"
            ],
            "behavioral": [
                "Drives Achievements",
                "Ethics & Compliance",
                "Timely Decision - Making"
            ],
            "technical": [
                "Business Development",
                "Key Account Management"
            ]
        }
    }
}

jd3 = {
    "id": "software-developer-002",
    "title": "Software Developer",
    "company": "Omantel",
    "description": {
        "overview": "We are seeking a Software Developer to work on exciting projects in ERP and cloud infrastructure domains, requiring strong programming and debugging skills.",
        "responsibilities": [
            "Diagnose network latency and intermittent issues",
            "Read and analyze log files",
            "Debug and performance tune SQL queries",
            "Contribute to ETL pipeline development",
            "Collaborate with ERP teams to enhance application performance",
            "Develop solutions in Python or Java",
            "Work with cloud infrastructure including Oracle Cloud Infrastructure (OCI)"
        ],
        "requirements": [
            "Bachelor's degree or equivalent experience in Computer Science or Engineering",
            "0-2+ years of experience in SQL/PL-SQL with excellent debugging skills",
            "Experience in diagnosing network latency and reading log files",
            "Good functional knowledge in ERP, Finance, HCM, or EBS domains",
            "Working experience with ERP systems such as Oracle EBS or Fusion",
            "Experience in performance tuning SQL and ETL pipelines",
            "Exposure to Oracle Cloud Infrastructure (OCI) is a plus",
            "Excellent interpersonal skills"
        ],
        "skills": [
            "SQL",
            "PL-SQL",
            "Python",
            "Java",
            "Oracle Cloud Infrastructure (OCI)",
            "ERP Systems",
            "ETL Pipelines"
        ],
        "location": "Bengaluru"
    }
}


# Data to be returned by the API
# job_descriptions=[
#   {
#     "id": "data-engineer-001",
#     "title": "Data Engineer",
#     "company": "Omantel",
#     "description": {
#       "overview": "We are seeking a talented data professional as a Data Engineer to join our Data Engineering team. This role requires a strong focus and experience in software development, multi-cloud based technologies, in memory data stores, and a strong desire to learn complex systems and new technologies.",
#       "responsibilities": [
#         "Design, develop, write, and modify code",
#         "Design, develop, maintain code, and support for web-based applications and ETLs using Python Fastapi",
#         "Support multi-cloud application development",
#         "Design and build complex systems that can scale rapidly",
#         "Design and implement effective service/product interfaces",
#         "Contribute to technical standards",
#         "Support development stages for application development",
#         "Influence company wide engineering standards",
#         "Conduct code reviews and develop documentation"
#       ],
#       "requirements": [
#         "Bachelor's degree in computer science, IT, or related field",
#         "1+ years of experience programming, building & supporting SaaS web applications",
#         "1+ years of experience programming in Python Fastapi",
#         "1+ years of experience with ETL workflow implementation",
#         "Knowledge of database architecture",
#         "Strong communication and collaboration skills"
#       ],
#       "skills": [
#         "Python",
#         "FastAPI",
#         "ETL",
#         "AWS",
#         "GCP",
#         "SQL",
#         "Github",
#         "Jenkins"
#       ]
#     }
#   },
#   {
#     "id": "senior-manager-growth-001",
#     "title": "Senior Manager, Growth Portfolio",
#     "company": "Omantel",
#     "description": {
#       "overview": "To develop and implement strategies to monetize data assets effectively, while also identifying and capitalizing on growth opportunities within specific customer segments.",
#       "position_info": {
#         "unit": "Business Unit",
#         "division": "Growth Portfolio",
#         "location": "HQ",
#         "grade": "L2",
#         "experience_required": "8-15 years"
#       },
#       "responsibilities": [
#         "Develop and refine strategies to identify high-value customer segments",
#         "Implement initiatives to monetize data assets",
#         "Drive revenue growth through targeted strategies",
#         "Cultivate strategic partnerships",
#         "Establish KPIs and metrics",
#         "Maintain deep knowledge of big data and analytics",
#         "Work closely with product management and marketing",
#         "Ensure alignment with company ethics",
#         "Build a results-driven team culture"
#       ],
#       "requirements": [
#         "Bachelor in relevant field",
#         "8 years of total experience",
#         "3 years in a managerial position"
#       ],
#       "competencies": {
#         "leadership": [
#           "Assertiveness and Conflict Resolution",
#           "Fostering Learning and Development",
#           "Inspiring and Leading Others",
#           "Leading Change and Cultivates Innovation",
#           "Visioning and Alignment"
#         ],
#         "behavioral": [
#           "Drives Achievements",
#           "Ethics & Compliance",
#           "Timely Decision - Making"
#         ],
#         "technical": [
#           "Business Development",
#           "Key Account Management"
#         ]
#       }
#     }
#   },
#   {
#     "id": "software-developer-002",
#     "title": "Software Developer",
#     "company": "Omantel",
#     "description": {
#       "overview": "We are seeking a Software Developer to work on exciting projects in ERP and cloud infrastructure domains, requiring strong programming and debugging skills.",
#       "responsibilities": [
#         "Diagnose network latency and intermittent issues",
#         "Read and analyze log files",
#         "Debug and performance tune SQL queries",
#         "Contribute to ETL pipeline development",
#         "Collaborate with ERP teams to enhance application performance",
#         "Develop solutions in Python or Java",
#         "Work with cloud infrastructure including Oracle Cloud Infrastructure (OCI)"
#       ],
#       "requirements": [
#         "Bachelor's degree or equivalent experience in Computer Science or Engineering",
#         "0-2+ years of experience in SQL/PL-SQL with excellent debugging skills",
#         "Experience in diagnosing network latency and reading log files",
#         "Good functional knowledge in ERP, Finance, HCM, or EBS domains",
#         "Working experience with ERP systems such as Oracle EBS or Fusion",
#         "Experience in performance tuning SQL and ETL pipelines",
#         "Exposure to Oracle Cloud Infrastructure (OCI) is a plus",
#         "Excellent interpersonal skills"
#       ],
#       "skills": [
#         "SQL",
#         "PL-SQL",
#         "Python",
#         "Java",
#         "Oracle Cloud Infrastructure (OCI)",
#         "ERP Systems",
#         "ETL Pipelines"
#       ],
#       "location": "Bengaluru"
#     }
#   }
# ]
@app.route('/upload', methods=['POST'])


def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    # Process the file if needed...
    data = {
    "Certifications": [
        {
            "Name": "Azure Data Fundamentals",
            "Organization": "Microsoft"
        },
        {
            "Name": "React for Beginners Course",
            "Organization": "Udemy"
        },
        {
            "Name": "Microsoft Powerbi bootcamp",
            "Organization": "Udemy"
        },
        {
            "Name": "Certified Ethical Hacking v10",
            "Organization": "EC-Council"
        },
        {
            "Name": "Core Desingner",
            "Organization": "Dataiku"
        }
    ],
    "Education": [
        {
            "Degree": "B.E Computer Science and Engineering",
            "EndDate": "05/2023",
            "GPA": "9.03 CGPA",
            "Institution": "Dr.Mahaligam College of Engineering and Technology",
            "Location": "Pollachi",
            "StartDate": "08/2019"
        },
        {
            "Degree": "12th",
            "EndDate": "2019",
            "GPA": "88.60%",
            "Institution": "Amrita Vidyalayam Senior Sec. School",
            "Location": "Coimbatore",
            "StartDate": "2018"
        },
        {
            "Degree": "10th",
            "EndDate": "2017",
            "GPA": "10 CGPA",
            "Institution": "Amrita Vidyalayam Senior Sec. School",
            "Location": "Coimbatore",
            "StartDate": "2016"
        }
    ],
    "Email": "tharunsrini22@gmail.com",
    "Full Name": "Tharun S C",
    "Location": "Coimbatore, India",
    "Phone Number": "+91 9585111212",
    "Skills": {
        "Soft Skills": [
            "Communication Skills",
            "Hard Working",
            "Self-Disciplined",
            "Great Team Player"
        ],
        "Technical Skills": [
            "Python",
            "SQL",
            "NoSql",
            "PowerBi",
            "PySpark",
            "Databricks",
            "ReactJs",
            "Flask",
            "Github",
            "Microsoft Azure",
            "ERP systems",
            "SAP",
            "Data Science",
            "Data Engineering",
            "Machine Learning",
            "Big Data",
            "Cloud Computing",
            "Artificial Intelligence",
            "Web Development",
            "Data Analysis",
            "Data Visualization",
            "OpenCV"
        ]
    },
    "Summary": "Passionate software developer specializing in data analytics and engineering, dedicated to integrating field insights for organizational advancement. Committed to scaling progress through innovative, data-driven solutions.",
    "Work Experience": [
        {
            "Company": "Kaar Technologies",
            "Description": [
                "Extensively trained in React, PowerBI, Python, Flask, and Databricks within the Data Science and Engineering department.",
                "Gained familiarity with ERP systems and SAP, acquiring insights across various modules.",
                "Actively engaged in practical experiences, shadowing senior professionals, and contributing to Proof of Concepts (POCs)."
            ],
            "EndDate": "Present",
            "Location": "Chennai",
            "Position": "Trainee (Data Engineering)",
            "StartDate": "09/2022"
        }
    ]
}
 


    return jsonify(data)

# Route to return the second AI response data
@app.route('/submit', methods=['GET','POST'])
def get_ai_response():
     # Simulate a delay of 4 seconds
    time.sleep(4)
    # Data for the second API
    result = {
        "result": {
            "Relevance Score": 60,
            "Relevant Experience": "1 year as Trainee at Kaar Technologies",
            "Short Description": "Tharun S C is a software developer with 1 year of experience in data engineering. His expertise lies in Python and SQL, both of which are mentioned as required skills in the job description. He is also proficient in data analytics and has worked on data engineering projects. Tharun holds an Azure Data Fundamentals certification from Microsoft and a B.E in Computer Science. His skills and experience make him a suitable candidate for the Data Engineer role."
        },
        "id": "6739b59e0f93508dc72c9741",
        "message": "Resume and job description successfully processed and stored."
    }
    # data = request.get_json()  # Capture the JSON payload
    # print("Received payload:", data)  # Log the received data
    return jsonify(result)


# @app.route('/job-description', methods=['GET'])
# def job_description():
#     # Sample job descriptions store (in production, this should be in a database)
    
#     return jsonify(job_descriptions)


 
# @app.route('/jobs', methods=['GET'])
# def get_all_jobs():
#     """Return all job descriptions with basic information"""
#     try:
#         job_summaries = [{
#             'id': job['id'],
#             'title': job['title'],
#             'company': job['company'],
#             'overview': job['description']['overview']
#         } for job in job_descriptions]
#         return jsonify({
#             'status': 'success',
#             'data': job_summaries
#         }), 200
#     except Exception as e:
#         print(f"Error fetching jobs: {str(e)}")
#         return jsonify({
#             'status': 'error',
#             'message': 'Failed to fetch jobs'
#         }), 500
 
# @app.route('/jobs/<job_id>', methods=['GET'])
# def get_job_by_id(job_id):
#     """Return detailed information for a specific job."""
#     try:
#         # Search for the job by ID in the job_descriptions list
#         job = next((job for job in job_descriptions if job['id'] == job_id), None)
        
#         if job:
#             return jsonify({
#                 'status': 'success',
#                 'data': job
#             }), 200
#         else:
#             return jsonify({
#                 'status': 'error',
#                 'message': 'Job not found'
#             }), 404
#     except Exception as e:
#         # Log the error for debugging
#         print(f"Error fetching job {job_id}: {str(e)}")
#         return jsonify({
#             'status': 'error',
#             'message': 'Failed to fetch job details'
#         }), 500

@app.route('/getfullname', methods=['GET'])
def get_full_name():
    try:
        # Fetch the last inserted document
        # latest_record = resumes_collection.find_one(sort=[("_id", -1)])
        # if not latest_record:
        #     return jsonify({"error": "No resume data found"}), 404
 
        # # Retrieve the full name
        # full_name = latest_record.get("parsed_resume", {}).get("Full Name", None)
        # if not full_name:
        #     return jsonify({"error": "Full Name not found in the parsed resume"}), 404
        full_name = "Tharun S C"
        # Return just the full name
        return jsonify({"Full Name": full_name}), 200
 
    except Exception as e:
        print(f"Error in /getfullname: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/candidates', methods=['GET'])
def get_candidates():
    data = {
        "data": [
            {
                "ai_response": {
                    "Relevance Score": 85,
                    "Relevant Experience": "2 years 9 months"
                },
                "parsed_resume": {
                    "Full Name": "DEVADHARSHINI B"
                }
            },
            {
                "ai_response": {
                    "Relevance Score": 92,
                    "Relevant Experience": "4 years 5 months"
                },
                "parsed_resume": {
                    "Full Name": "ARUN KUMAR S"
                }
            },
            {
                "ai_response": {
                    "Relevance Score": 78,
                    "Relevant Experience": "1 year 3 months"
                },
                "parsed_resume": {
                    "Full Name": "PRIYA R"
                }
            }
        ],
        "message": "Records fetched successfully"
    }

    return jsonify(data)


@app.route('/jd1', methods=['GET'])
def get_jd1():
    return jsonify(jd1)

@app.route('/jd2', methods=['GET'])
def get_jd2():
    return jsonify(jd2)

@app.route('/jd3', methods=['GET'])
def get_jd3():
    return jsonify(jd3)


if __name__ == '__main__':
    app.run(debug=True)