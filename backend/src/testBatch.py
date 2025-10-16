import sys
import os
sys.path.append(os.path.dirname(__file__))

from assignment_functions.assignment_queries import create_batch_assignment
from insert_data.add_data import add_assignment
from insert_data.insert_functions import insert_assignment

def test_batch_assignment():
    # Test data
    teacher_ID = "te_john_doe_123"
    assignment_data = [
        {
            "class_ID": "cl_math_7a_202501010900_202501010945_dur_45_rm_a101",
            "date": "2025-01-15",
            "notes": "Test assignment 1",
            "status": "searching"
        },
        {
            "class_ID": "cl_science_8b_202501011000_202501011045_dur_45_rm_a102", 
            "date": "2025-01-15",
            "notes": "Test assignment 2",
            "status": "searching"
        }
    ]
    
    print("Testing create_batch_assignment...")
    result = create_batch_assignment(teacher_ID, assignment_data)
    print("Result:", result)
    
    return result

def test_add_assignment():
    # Test individual assignment creation
    print("\nTesting add_assignment...")
    result = add_assignment(
        date="2025-01-15",
        status="searching", 
        class_ID="cl_math_7a_202501010900_202501010945_dur_45_rm_a101",
        teacher_ID="te_john_doe_123",
        substitute_ID=None,
        notes="Test notes",
        conn=None
    )
    print("Result:", result)
    return result

if __name__ == "__main__":
    # Test individual function first
    test_add_assignment()
    
    # Then test batch function
    test_batch_assignment()