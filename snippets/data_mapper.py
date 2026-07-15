from typing import Dict, Any

def validate_and_map_data(data: Dict[str, Any]) -> Dict[str, Any]:
    # Define the expected structure and data types for each field
    expected_structure = {
        "project_title": str,
        "job_type": str,
        "company_name": str,
        "position": str,
        "skills_required": list,
        "location": str,
        "duration": str,
        "payment_method": str,
        "description": str,
        "requirements": dict
    }

    # Validate and map the data
    mapped_data = {}
    for key, expected_type in expected_structure.items():
        if key not in data:
            raise ValueError(f"Missing required field: {key}")
        value = data[key]
        if not isinstance(value, expected_type):
            raise TypeError(f"Incorrect type for field '{key}': expected {expected_type.__name__}, got {type(value).__name__}")
        mapped_data[key] = value

    # Additional validation and mapping logic can be added here
    # For example, validating the format of email addresses or phone numbers

    return mapped_data

# Example usage:
data = {
    "project_title": "【急募・長期案件】不動産査定SaaSのAI自動化・Rails開発エンジニア募集",
    "job_type": "Full-time",
    "company_name": "Tech Innovations Inc.",
    "position": "Rails Development Engineer",
    "skills_required": ["Ruby", "Rails", "JavaScript"],
    "location": "San Francisco, CA",
    "duration": "Long-term",
    "payment_method": "Hourly",
    "description": "We are looking for a skilled Rails developer to automate real estate valuations using AI.",
    "requirements": {
        "education": "Bachelor's degree in Computer Science or related field",
        "experience": "3+ years of experience with Ruby on Rails"
    }
}

try:
    validated_data = validate_and_map_data(data)
    print("Data is valid and mapped successfully.")
except (ValueError, TypeError) as e:
    print(f"Validation error: {e}")