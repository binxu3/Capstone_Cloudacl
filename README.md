# Capstone_Cloudacl

## Project Track

Track 1 - Data Mining and Analysis System for Cloudacl

## Project Objective:

- Use knowledge both in **data scientist** and **data engineer** field
- Have a deep insight for an ETL process and understand how it works
- Understand how cloud computing such as **AWS** could help in manipulating bigdata 
- Learn how to use data scientific cycle to do data analysis
- Learn how to build up a data pipeline to solve real problem and what problems need to be fixed

## Project Introduction:

### About the company:

Cloudacl is the leading provider of security and infrastructure services that make the Internet safer through integrated Web content filtering. Cloudacl services enable family, school and small business user to secure their networks from online threats, reduce costs and enforce Internet-use policies.

### About our technology

#### Cloud based services

Cloudacl is powered by a cloud based service hosted on Amazon EC2. It is based on Hadoop software stack and can scale out to thousands of servers, providing high realtime performance and powerful analytical backend at the same time.

### Website classifier

Cloudacl uses the state-of-the-art machine learning techniques to automatically classify websites into different categories. Our classifier works under the standard cloud-computing platform (i.e. mapreduce under hadoop), so it can scale up to classify  millions of websites. Moreover, it uses very sophisticated natural language processing techniques to extract classification signals from website content, so it can support many international languages in addition to English.

## Team Members:

Bin Xu
Liu Yi
Si jie
Liu Chen Chen
Dong Ze Yu

## Data Format:

Web Log

### Sample Data:

137.207.69.207 - - [06/Mar/2017:00:00:00 +0000] "GET /axis2/services/WebFilteringService/getCategoryByUrl?app=chrome_antiporn&ver=0.19.7.1&url=https%3A//www.youtube.com/watch%3Fv%3DNBcUz5TUsHQ&cat=media-streaming HTTP/1.1" 200 133 "-" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

130.105.213.119 - - [06/Mar/2017:00:00:00 +0000] "GET /axis2/services/WebFilteringService/getCategoryByUrl?app=chrome_antiporn&ver=0.19.7.1&url=https%3A//www.google.com.ph/_/chrome/newtab%3Fespv%3D2%26ie%3DUTF-8&cat=search-engine HTTP/1.1" 200 133 "-" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

## Project Proposal of Bin Xu
- Use AWS S3 to read in data and do data cleaning and transformation in EMR

- 
Category Mapping
===========
 0:  unknown
 1:  hacking
 2:  phishing-and-fraud
 3:  botnet
 4:  malware
 5:  spyware-and-adware
 6:  keylogger-and-monitoring
 7:  peer2peer
 8:  media-streaming
 9:  online-storage
 10: abortion
 11: adult-and-pornography
 12: sex-education
 13: nudity
 14: abused-drugs
 15: marijuana
 16: healthy-and-medicine
 17: real-estate
 18: internet-security
 19: financial-service
 20: business-and-economy
 21: computer-information
 22: auctions
 23: shopping
 24: cult-and-occult
 25: travel
 26: home-garden
 27: military
 28: social-networking
 29: dead-sites
 30: stock-and-tool
 31: training-and-tool
 32: dating
 33: religion
 34: entertainment-and-art
 35: personal-site-and-blog
 36: legal
 37: local-info
 38: job-search
 39: gambling
 40: translation
 41: research-reference
 42: software-download
 43: game
 44: philosophy-and-political
 45: weapon
 46: pay2surf
 47: hunting-and-fishing
 48: society
 49: educational-institution
 50: online-greeting
 51: sport
 52: swimsuits-&-intimate-apparel
 53: questionable
 54: kid
 55: search-engine
 56: internet-portal
 57: online-advertisement
 58: web-mail
 59: envasion-proxy
 60: music
 61: government
 62: news-and-media
 63: content-delivery-network
 64: internet-communication
 65: spam-comfirmed
 66: spam-url
 67: spam-unconfirmed
 68: http-proxy
 69: dynamically-content
 70: parked-domain
 71: alcohol-and-tobacco
 72: private-ip
 73: image-and-video-search
 74: fashion-and-beauty
 75: recreation-and-hobbies
 76: motor-vehicle
 77: web-hosting
