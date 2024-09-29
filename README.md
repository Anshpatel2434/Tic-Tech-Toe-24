<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StudyShare README</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #e0e0e0;
            background-color: #1a1a1a;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #58a6ff;
            border-bottom: 2px solid #58a6ff;
            padding-bottom: 10px;
        }
        h2 {
            color: #79c0ff;
        }
        code {
            background-color: #2a2a2a;
            border: 1px solid #444;
            border-radius: 3px;
            padding: 2px 5px;
            font-family: 'Courier New', Courier, monospace;
        }
        pre {
            background-color: #2a2a2a;
            border: 1px solid #444;
            border-radius: 3px;
            padding: 10px;
            overflow-x: auto;
        }
        ul {
            padding-left: 20px;
        }
        .video-container {
            position: relative;
            padding-bottom: 56.25%;
            padding-top: 30px;
            height: 0;
            overflow: hidden;
            margin-bottom: 20px;
        }
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .emoji {
            font-size: 1.2em;
            margin-right: 5px;
        }
        .feature-icon {
            margin-right: 10px;
            color: #58a6ff;
        }
    </style>
</head>
<body>
    <h1><span class="emoji">📚</span> StudyShare</h1>
    <h2><span class="emoji">🚀</span> Project Description</h2>
    <p>StudyShare is an innovative E-library platform designed to revolutionize the digital reading and learning experience. Our platform aims to create a vibrant community of readers and learners, providing a seamless environment for accessing, sharing, and discussing educational materials.</p>
    <h2><span class="emoji">✨</span> Key Features</h2>
    <ul>
        <li><i class="fas fa-comments feature-icon"></i><strong>Real-Time Communication System:</strong> WebSocket-powered chat system for instant user interactions.</li>
        <li><i class="fas fa-chart-line feature-icon"></i><strong>Advanced User Analytics:</strong> Heatmap system and real-time dashboard analysis for deep user insights.</li>
        <li><i class="fas fa-star feature-icon"></i><strong>Dynamic Rating and Viewing System:</strong> Real-time updates on content popularity.</li>
        <li><i class="fas fa-brain feature-icon"></i><strong>Intelligent Recommendation Engine:</strong> Personalized content suggestions using Random Forest Regression and NLP.</li>
        <li><i class="fas fa-trophy feature-icon"></i><strong>User Leaderboard:</strong> Competitive ranking system based on user ratings.</li>
        <li><i class="fas fa-search feature-icon"></i><strong>Powerful Search Functionality:</strong> Advanced search and filter options for efficient resource discovery.</li>
        <li><i class="fas fa-file-upload feature-icon"></i><strong>Seamless File Management:</strong> Easy upload and organization of study materials.</li>
    </ul> 
    <h2><span class="emoji">⚙</span> Installation</h2>
    <h3>Backend Setup</h3>
    <pre><code>git clone https://github.com/Anshpatel2434/Tic-Tech-Toe-24.git
cd backend
./myenv/Scripts/activate.bat
pip install scikit-learn
cd admin
py manage.py runserver
</code></pre>  
    <h3>Frontend Setup</h3>
    <pre><code>cd frontend
npm install
npm add react-calendar-heatmap
npm run dev
</code></pre> 
    <h2><span class="emoji">🎥</span> Project Demo</h2>
    <div class="video-container">
        <iframe src="https://www.loom.com/embed/ed274b29a6804ceaa96627c59e5f76f0?sid=3e5e7532-9ada-4c8c-98dc-ba633a9ef8c7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    </div>
    <p>Watch our project demo: <a href="https://www.loom.com/share/ed274b29a6804ceaa96627c59e5f76f0?sid=3e5e7532-9ada-4c8c-98dc-ba633a9ef8c7" target="_blank">StudyShare Demo Video</a></p>
    <h2><span class="emoji">🖼</span> Images</h2>
    <p>
        <!-- Replace with actual project screenshots -->
        <img src="https://drive.google.com/file/d/10sDx_FKuYyXvpvmPfU-CUng2ps2EGqwS/view?usp=drive_link" alt="StudyShare Dashboard" style="max-width: 100%; height: auto; margin-bottom: 10px;">
        <img src="https://drive.google.com/file/d/15giDCPcawxT6xrs1nEXd9ZUt2OgSU9Fo/view?usp=drive_link" alt="StudyShare Chat Interface" style="max-width: 100%; height: auto;">
        <img src="https://drive.google.com/file/d/1oBTiw8dtZzMjQHLY0pHvHOKEo8ym495t/view?usp=drive_link" alt="StudyShare Chat Interface" style="max-width: 100%; height: auto;">
        <img src="https://drive.google.com/file/d/1Rr2BBNHW_aIzTqd1RiIW9tW-pNNemTwC/view?usp=drive_link" alt="StudyShare Chat Interface" style="max-width: 100%; height: auto;">
    </p>
    <h2><span class="emoji">🤝</span> Contributing</h2>
    <p>We welcome contributions to StudyShare! Please read our contributing guidelines to get started.</p>
</body>
</html>
