import subprocess
import os
import sys

def run_tests(step_folder):
    test_files = [f for f in os.listdir(step_folder) if f.endswith('.json')]
    results = []
    for test_file in test_files:
        path = os.path.join(step_folder, test_file)
        proc = subprocess.run(
            ['python', 'main.py', path],
            capture_output=True,
            text=True
        )
        # Determine expected result from filename
        if 'invalid' in test_file:
            expected = 1
        elif 'valid' in test_file:
            expected = 0
        else:
            expected = None  # Unknown expectation

        actual = proc.returncode
        if expected is None:
            status = 'UNKNOWN'
        elif actual == expected:
            status = '✅'
        else:
            status = '❌'
        results.append(f"{status} {test_file}: expected sys code {expected}, got {actual} - {proc.stdout.strip()}")
    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_runner.py <step_number|all>")
        sys.exit(1)
    arg = sys.argv[1]
    if arg == "all":
        for step in range(1, 5):
            folder = f"tests/step{step}"
            if not os.path.isdir(folder):
                print(f"Test folder not found: {folder}")
                continue
            print(f"\n=== Step {step} ===")
            for result in run_tests(folder):
                print(result)
    else:
        folder = f"tests/step{arg}"
        if not os.path.isdir(folder):
            print(f"Test folder not found: {folder}")
            sys.exit(1)
        print(f"\n=== Step {arg} ===")
        for result in run_tests(folder):
            print(result)