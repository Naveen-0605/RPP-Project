# Import the DeepFace library
from deepface import DeepFace

# List of image paths you want to analyze
image_paths = ["1.jpg", "2.jpg", "3.jpg"]  # Add your image file names here

# Analyze each image
for image_path in image_paths:
    try:
        print(f"Analyzing {image_path}...")
        result = DeepFace.analyze(img_path=image_path, actions=["age", "gender", "emotion", "race"])
        
        # Check if any persons were detected
        if not result:
            print(f"No faces detected in {image_path}.")
            continue
        
        # Print the analysis result in a structured format
        for idx, person in enumerate(result):
            print(f"Person {idx + 1}:")
            print(f"  Age: {person['age']}")
            print(f"  Region: {person['region']}")
            print(f"  Face Confidence: {person['face_confidence']}")
            print(f"  Gender: {person['dominant_gender']} (Woman: {person['gender']['Woman']}, Man: {person['gender']['Man']})")
            print(f"  Emotion: {person['dominant_emotion']} (Angry: {person['emotion']['angry']}, Disgust: {person['emotion']['disgust']}, Fear: {person['emotion']['fear']}, Happy: {person['emotion']['happy']}, Sad: {person['emotion']['sad']}, Surprise: {person['emotion']['surprise']}, Neutral: {person['emotion']['neutral']})")
            print(f"  Race: {person['dominant_race']} (Asian: {person['race']['asian']}, Indian: {person['race']['indian']}, Black: {person['race']['black']}, White: {person['race']['white']}, Middle Eastern: {person['race']['middle eastern']}, Latino Hispanic: {person['race']['latino hispanic']})")
            print("\n")  # Add a newline for better separation between persons
    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")
