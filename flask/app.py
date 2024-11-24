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
                },
                "job_id": "data-engineer-001"
            },
            {
                "ai_response": {
                    "Relevance Score": 92,
                    "Relevant Experience": "4 years 5 months"
                },
                "parsed_resume": {
                    "Full Name": "ARUN KUMAR S"
                },
                "job_id": "software-developer-002"
            },
            {
                "ai_response": {
                    "Relevance Score": 78,
                    "Relevant Experience": "1 year 3 months"
                },
                "parsed_resume": {
                    "Full Name": "PRIYA R"
                },
                "job_id": "senior-manager-growth-001"
            }
        ],
        "message": "Records fetched successfully"
    }

    return jsonify(data)

@app.route('/profile', methods=['POST'])
def get_profile():
    # Extract the candidate's full name from the request
    data = request.get_json()
    # full_name = data.get('full_name', '')
    full_name = data.get('full_name', '').lower().strip()

    # Simulated profile data for multiple candidates
    profiles = [
        {
            "Full Name": "B DEVADHARSHINI",
            "Email": "devabaskar09@gmail.com",
            "Phone Number": "+91-9578120402",
            "Location": "Trichy, Tamil Nadu",
            "Summary": "I am a highly competent IT professional with 2 year and 9 months work experience...",
            "Education": [
                {
                    "Degree": "B.E.",
                    "Institution": "K.Ramakrishnan College Of Engineering",
                    "Location": "Trichy, Tamil Nadu",
                    "StartDate": "2017",
                    "EndDate": "2021",
                    "GPA": "9.12"
                }
            ],
            "Certifications": [
                {
                    "Name": "Google Cloud Certified Professional Data Engineer",
                    "Organization": "Google Cloud"
                },
                {
                    "Name": "Google Cloud Certified Associate Cloud Engineer",
                    "Organization": "Google Cloud"
                },
                {
                    "Name": "First Level Of Certification in Japanese Language Course",
                    "Organization": "N-5"
                }
            ],
            "Work Experience": [
                {
                    "Company": "Wipro Ltd.",
                    "Title": "Data Engineer | Developer",
                    "Location": "Chennai, Tamil Nadu",
                    "StartDate": "Feb 2022",
                    "EndDate": "Current",
                    "Description": "As a part of Insurance Data Hub, built a data platform on GCP..."
                },
                {
                    "Company": "Accenture Solutions Pvt Ltd.",
                    "Title": "Application Development Associate | Developer",
                    "Location": "Chennai, Tamil Nadu",
                    "StartDate": "May 2021",
                    "EndDate": "Dec 2021",
                    "Description": "Fulfilled tasks and jobs delegated by project manager..."
                },
                {
                    "Company": "Cognizant Solutions Pvt Ltd.",
                    "Title": "Intern",
                    "Location": "Chennai, Tamil Nadu",
                    "StartDate": "March 2021",
                    "EndDate": "April 2021",
                    "Description": "Undergone series of webinars, quizzes, SME interactions..."
                }
            ],
            "Skills": {
                "Technical Skills": [
                    "Python",
                    "SQL (Postgres, MySQL, CloudSQL)",
                    "GCP (GCS, Biquery, CloudSQL, Dataflow)",
                    "ETLs",
                    "GIT",
                    "JIRA",
                    "Shell Scripting"
                ],
                "Soft Skills": []
            }
        },
        {
            "Full Name": "PRIYA R",
            "Email": "ananya.sharma@example.com",
            "Phone Number": "+91-9876543210",
            "Location": "Mumbai, Maharashtra",
            "Summary": "Experienced senior manager with a proven track record in leading growth portfolios and strategic initiatives...",
            "Education": [
                {
                    "Degree": "MBA",
                    "Institution": "Indian Institute of Management, Bangalore",
                    "Location": "Bangalore, Karnataka",
                    "StartDate": "2014",
                    "EndDate": "2016",
                    "GPA": "8.9"
                }
            ],
            "Certifications": [
                {
                    "Name": "PMP (Project Management Professional)",
                    "Organization": "PMI"
                },
                {
                    "Name": "Certified Scrum Master",
                    "Organization": "Scrum Alliance"
                }
            ],
            "Work Experience": [
                {
                    "Company": "Reliance Industries",
                    "Title": "Senior Manager - Growth Portfolio",
                    "Location": "Mumbai, Maharashtra",
                    "StartDate": "Jan 2020",
                    "EndDate": "Current",
                    "Description": "Led a cross-functional team to deliver high-impact projects..."
                },
                {
                    "Company": "Tata Consultancy Services",
                    "Title": "Project Manager",
                    "Location": "Mumbai, Maharashtra",
                    "StartDate": "Aug 2016",
                    "EndDate": "Dec 2019",
                    "Description": "Managed global teams to ensure successful project delivery..."
                }
            ],
            "Skills": {
                "Technical Skills": [
                    "Project Management",
                    "Agile Methodologies",
                    "Team Leadership"
                ],
                "Soft Skills": ["Strategic Thinking", "Team Collaboration", "Problem Solving"]
            }
        },
        {
            "Full Name": "ARUN KUMAR S",
            "Email": "rajesh.kumar@example.com",
            "Phone Number": "+91-9876541234",
            "Location": "Bangalore, Karnataka",
            "Summary": "A software developer passionate about building scalable and efficient solutions...",
            "Education": [
                {
                    "Degree": "B.Tech in Computer Science",
                    "Institution": "National Institute of Technology, Karnataka",
                    "Location": "Surathkal, Karnataka",
                    "StartDate": "2015",
                    "EndDate": "2019",
                    "GPA": "9.1"
                }
            ],
            "Certifications": [
                {
                    "Name": "AWS Certified Solutions Architect",
                    "Organization": "Amazon Web Services"
                },
                {
                    "Name": "Microsoft Certified Azure Developer",
                    "Organization": "Microsoft"
                }
            ],
            "Work Experience": [
                {
                    "Company": "Infosys",
                    "Title": "Software Developer",
                    "Location": "Bangalore, Karnataka",
                    "StartDate": "Jul 2019",
                    "EndDate": "Current",
                    "Description": "Developed and maintained enterprise-level web applications..."
                }
            ],
            "Skills": {
                "Technical Skills": [
                    "Java",
                    "Spring Boot",
                    "Angular",
                    "React",
                    "Docker",
                    "Kubernetes"
                ],
                "Soft Skills": ["Analytical Thinking", "Problem Solving"]
            }
        }
    ]
    # Flexible name matching logic
    for profile in profiles:
        profile_name = profile["Full Name"].lower()
        # Check if all words in the request name are in the profile name
        if all(word in profile_name for word in full_name.split()):
            return jsonify(profile)
    
    return jsonify({"message": "Profile not found"}), 404




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