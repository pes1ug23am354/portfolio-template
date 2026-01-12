from supabase import create_client, Client

SUPABASE_URL = "https://zykllxixkwlfdnamxxgf.supabase.co" 
SUPABASE_KEY = "sb_publishable_CDJSnbE8SC8Q5UjZUmFMyw_8di6oVZf" 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

## Step 1: Create a storage bucket
#bucket_name = "imgs2" # Name of the bucket to be created
#try:
 #   response = supabase.storage.create_bucket(bucket_name,   
  #  options={
   #     "public": True, # Make the bucket public
   #     "allowed_mime_types": ["image/png"], # Allow only PNG images
    #    "file_size_limit": 1024*1024, # Limit file size to 1MB
   # }
#    )
 #print(f"Bucket '{bucket_name}' created successfully.")
#except Exception as e:
 #   print(f"Bucket creation error: {e}")

# Step 2: Upload an image to the bucket

#image_path = "/Users/vivannaik/Desktop/cc lab-1/cat.png"
#image_name = "cat.png"

#try:
 #   with open(image_path, "rb") as f:
  #      response = supabase.storage.from_("imgs2").upload(
   #         path=image_name,
    #        file=f,
     #       file_options={
      #          "content-type": "image/png",
       #         "cache-control": "3600",
        #        "upsert": "True"
         #   }
       # )

    #print("Image uploaded successfully")

#except Exception as e:
 #   print(f"Image upload error: {e}")


# # Step 3: Get the public URL of the image
# Step 3: Get the public URL of the image

try:
    public_url = supabase.storage.from_("imgs2").get_public_url("cat.png")
    print(f"Public URL of the image: {public_url}")

except Exception as e:
    print(f"Error getting public URL: {e}")

