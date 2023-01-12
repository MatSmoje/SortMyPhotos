## What is it? 
It is a small script that helps me to organize my photographs by deleting the duplicates and creating and storing the images in folders with the year where it was taken. 

### The Problem
I took many photos and my ex-girlfriend used to send me her pictures also. And she asked me to send mines. Therefore, we got our collapsed our cellphone storage and we got repeated pictures. 

### The Solution
- The script makes a list of the path of each picture. Then it gets their hash and deletes the repeated hash.

#### To Consider
Eventually, there might be *hash collision*, so you could get two different images with same hash. The hash algoritm that I used is md5.
Other hash algorithm has less probability of hash collision:
- MD5: 1.47E-29  
- SHA1: 1E-45  
- SHA256: 4.3*E-60  