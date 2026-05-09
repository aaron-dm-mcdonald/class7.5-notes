from locust import HttpUser, task

class WebsiteUser(HttpUser):
    # Class-level variables are shared across all simulated users.
    region_map = {}
    region_counter = 0

    def on_start(self):
        # Instance-level variable unique to each simulated user
        self.last_region = None

    @task
    def check_metadata(self):
        # Hits the JSON metadata endpoint from your startup script
        response = self.client.get("/metadata")
        data = response.json()
        region = data.get("region")

        # 1. Discover and label regions globally
        if region not in WebsiteUser.region_map:
            WebsiteUser.region_counter += 1
            WebsiteUser.region_map[region] = f"Region {chr(64 + WebsiteUser.region_counter)}"
            print(f"NEW: {region} -> {WebsiteUser.region_map[region]}")

        # 2. Only log if the region changes for this specific user.
        if self.last_region is not None and region != self.last_region:
            label = WebsiteUser.region_map[region]
            print(f"--- SHIFT: {label} ({region}) ---")
        
        # Update the user's state for the next request
        self.last_region = region