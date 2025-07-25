import json
from difflib import unified_diff

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_jobs(dev_jobs, prod_jobs):
    all_job_names = set(dev_jobs.keys()).union(prod_jobs.keys())
    for job in sorted(all_job_names):
        print(f"\n=== Comparing Job: {job} ===")
        dev = json.dumps(dev_jobs.get(job, {}), indent=4).splitlines()
        prod = json.dumps(prod_jobs.get(job, {}), indent=4).splitlines()

        diff = list(unified_diff(dev, prod, fromfile='DEV', tofile='PROD', lineterm=''))
        if diff:
            print("\n".join(diff))
        else:
            print("✅ No differences found.")

if __name__ == "__main__":
    dev_jobs = load_json('dev_jobs.json')
    prod_jobs = load_json('prod_jobs.json')
    compare_jobs(dev_jobs, prod_jobs)
