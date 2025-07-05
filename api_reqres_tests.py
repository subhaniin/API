import requests

# Step 1 - GET home page
resp1 = requests.get("https://reqres.in/")
assert resp1.status_code == 200
assert "<html" in resp1.text.lower()
print("✅ Step 1 passed: Homepage reachable and contains HTML")

# Step 2 - GET /signup page
resp2 = requests.get("https://reqres.in/signup")
assert resp2.status_code == 200
print("✅ Step 2 passed: Signup page reachable")

# Step 3 - GET user by ID
resp3 = requests.get("https://reqres.in/api/users/2")
data = resp3.json().get("data", {})

assert resp3.status_code == 200
assert data.get("id") == 2
assert "@" in data.get("email", "")
assert data.get("avatar", "").startswith("https://")
print("✅ Step 3 passed: User 2 data is valid and complete")