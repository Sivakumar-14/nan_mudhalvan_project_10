                                  CURRENCY NOTE AUTHENTICATION


 PURPOSE :  The primary aim of this project is to develop a reliable and efficient method for 
            authenticating currency notes using image processing and feature matching. By 
            comparingkey features in genuine and test note images, this approach helps in 
            detecting counterfeit notes with minimal manual intervention.


                                    TECHNOLOGIES USED


PYHTON –   The core programming language used to implement the system due to its simplicity and 
           extensive library support for image processing and machine learning tasks.

OPENCV –   A powerful computer vision library used for feature detection, keypoint extraction, 
           image preprocessing, and matching techniques essential for currency note 
           authentication.

NUMPY –    Utilized for efficient numerical computations and matrix operations, which are 
           integral to processing and analyzing image data.

MATPLOTLIB –   Employed to visualize keypoints, matching results, and comparative outputs, 
               aiding in both debugging and result interpretation.



                                    USAGE


  Load genuine and test note images

    
The system begins by loading two images: one of a known genuine currency note and another of the note to be tested for authenticity.

Extract keypoints and descriptors using ORB  :  ORB (Oriented FAST and Rotated BRIEF) detects 
                                                important features (keypoints) in both images 
                                                and generates descriptors—compact 
                                                representations of those features—for matching.

Match the extracted features using BFMatcher  :  The Brute-Force Matcher compares descriptors 
                                                 from both images Hamming distance find the best 
                                                 matches between corresponding keypoints.

Calculate a similarity score  : A similarity score is computed by measuring the ratio of "good" 
                                matches to total keypoints. This score indicates how closely the 
                                test note resembles the genuine one.

Display the top feature matches  :  A visual output shows the best-matching features between the 
                                    two notes, helping users confirm the matching process 
                                    visually.

Provide a simple decision on authenticity  : Based on the similarity score and a defined 
                                             threshold, the system decides whether the test note 
                                             is genuine or counterfeit.


CONCLUSION  :  This project provides a straightforward yet effective approach to currency note 
               authentication using feature matching techniques. By leveraging ORB's speed and 
               accuracy, it offers a scalable solution for detecting counterfeit notes, 
               potentially aiding in secure financial transactions and fraud prevention.


               






            
