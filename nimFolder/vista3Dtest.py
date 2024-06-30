import io
import os
import requests
import shutil
import tempfile
import zipfile

invoke_url = "https://health.api.nvidia.com/v1/medicalimaging/nvidia/vista-3d"

headers = {
    "Authorization": "Bearer $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",
}

sample = "example-1"
# in future, run each image from dataset individually within payload dictionary
payload = {
    "image": f"https://assets.ngc.nvidia.com/products/api-catalog/vista3d/{sample}.nii.gz",
    "prompts": {
        "classes": ["liver", "spleen"]
    }
}

# re-use connections
session = requests.Session()
response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
with tempfile.TemporaryDirectory() as temp_dir:
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(temp_dir)
    shutil.move(os.path.join(temp_dir, os.listdir(
        temp_dir)[0]), f"{sample}_seg.nrrd")

print("---------------------------------------------------------------")
print(f"Input Image: {payload['image']}")
print(f"Class Prompts: {payload.get('prompts', {}).get('classes')}")
print(f"Response Mask: {sample}_seg.nrrd")
print("")
