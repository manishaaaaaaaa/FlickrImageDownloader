#import necessary libraries
import requests
import os

#define a function to search photos on flickr

def search_flickr(query,api_key,num_images=100):
    #base URl for the flickr API
    url='https://api.flickr.com/services/rest/'

    #parameters for the api reuest
    params={'method':'flickr.photos.search',#Api method 
            'api_key':api_key,#APi key for authentication
            'text':query,
            'tags':'bird',#change the tag as per your need i.e what image you want to download
            'sort':'relevance',
            'per-image':num_images,
            'format':'json',
            'nojsoncallback':1 #prevents JSON response
            }
    #send a GET request to the FLickr API
    response=requests.get(url,params=params)
    if response.status_code ==200:
        #parse JSON response and extract the list of photos
        return response.json()['photos']['photo']
    else:
        print("Failed to fetch flickr API.")
        return[]
    #DEfine a function to construct the URL of the photo
def get_photo_url(photo,size='large'):
    url=f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}"
    if size=='large':
        url+='_b.jpg'
    elif size=='medium':
        url+='_z.jpg'
    else:
        url+='_.jpg'   
    return url
def download_images(photos_list,directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i,photo in enumerate(photos_list):
        img_url=get_photo_url(photo)
        img_path=os.path.join(directory,f'image_{i+1}.jpg')
        with open(img_path,'wb') as img_file:
            img_file.write(requests.get(img_url).content)
            #define the main fucnction
def main():
    query='bird'
    api_key='047bb4f78c133310327faef11139d1d4'

    num_images=10
    #search photos in flickr
    photo_list=search_flickr(query,api_key,num_images)
    download_images(photo_list,'birdd_images')   #downloaded images will be saved to this folder 
if __name__ =='__main__':
    main()           


    