var jsonData = pm.response.json();
pm.environment.set("bearer_token", jsonData.access_token);
