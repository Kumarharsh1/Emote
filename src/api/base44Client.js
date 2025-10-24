// Base44 API Client with environment variables
const BASE_URL = process.env.BASE44_API_URL || "https://app.base44.com/api/apps/YOUR_APP_ID_HERE";
const API_KEY = process.env.BASE44_API_KEY || "your_api_key_here";

export const base44 = {
    entities: {
        Detection: {
            list: async (sort = "-created_date", limit = 50) => {
                const response = await fetch(`${BASE_URL}/entities/Detection?sort=${sort}&limit=${limit}`, {
                    headers: {
                        "api_key": API_KEY,
                        "Content-Type": "application/json"
                    }
                });
                return await response.json();
            },
            create: async (data) => {
                const response = await fetch(`${BASE_URL}/entities/Detection`, {
                    method: "POST",
                    headers: {
                        "api_key": API_KEY,
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                });
                return await response.json();
            },
            update: async (entityId, updateData) => {
                const response = await fetch(`${BASE_URL}/entities/Detection/${entityId}`, {
                    method: "PUT",
                    headers: {
                        "api_key": API_KEY,
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(updateData)
                });
                return await response.json();
            },
            delete: async (entityId) => {
                const response = await fetch(`${BASE_URL}/entities/Detection/${entityId}`, {
                    method: "DELETE",
                    headers: {
                        "api_key": API_KEY,
                        "Content-Type": "application/json"
                    }
                });
                return await response.json();
            }
        }
    },
    integrations: {
        Core: {
            UploadFile: async ({ file }) => {
                const formData = new FormData();
                formData.append("file", file);
                
                const response = await fetch(`${BASE_URL}/integrations/Core/UploadFile`, {
                    method: "POST",
                    headers: {
                        "api_key": API_KEY,
                    },
                    body: formData
                });
                return await response.json();
            },
            InvokeLLM: async ({ prompt, file_urls, response_json_schema }) => {
                const response = await fetch(`${BASE_URL}/integrations/Core/InvokeLLM`, {
                    method: "POST",
                    headers: {
                        "api_key": API_KEY,
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        prompt,
                        file_urls,
                        response_json_schema
                    })
                });
                return await response.json();
            }
        }
    }
};

export default base44;
