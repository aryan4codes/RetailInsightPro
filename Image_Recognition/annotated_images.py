import cv2

# Define the list of image paths and bounding boxes
image_data = [
    ("shelf_images/IMG-20240206-WA0010.jpg", [
         [(20, 271), (183, 358)],
    [(22, 371), (22, 371)],
    [(23, 373), (189, 453)],
    [(24, 466), (195, 559)],
    [(32, 565), (192, 655)],
    [(22, 667), (193, 755)],
    [(197, 252), (371, 340)],
    [(199, 355), (377, 431)],
    [(203, 445), (368, 532)],
    [(217, 543), (359, 637)],
    [(212, 662), (359, 742)],
    [(219, 742), (343, 790)],
    [(383, 387), (544, 490)],
    [(377, 489), (540, 584)],
    [(374, 589), (498, 714)],
    [(382, 723), (494, 785)],
    [(554, 413), (671, 517)],
    [(548, 521), (663, 624)],
    [(647, 629), (786, 734)],
    [(678, 525), (807, 630)],
    [(682, 423), (800, 525)],
    [(679, 317), (795, 416)],
    [(557, 309), (665, 409)],
    [(805, 312), (912, 423)],
    [(816, 430), (917, 524)],
    [(809, 527), (919, 618)],
    [(780, 625), (901, 723)],
    [(791, 726), (889, 792)],
    [(924, 273), (1051, 376)],
    [(916, 383), (1041, 490)],
    [(923, 497), (1049, 590)],
    [(921, 594), (1043, 714)],
    [(900, 712), (1012, 777)],
    [(1062, 277), (1189, 374)],
    [(1062, 386), (1177, 483)],
    [(1046, 490), (1166, 596)],
    [(1043, 601), (1165, 710)],
    [(1021, 714), (1135, 783)],
    [(402, 294), (526, 388)],
    [(519, 628), (633, 725)],
    ]),
    ("shelf_images/IMG-20240206-WA0011.jpg", [
         [(328, 209), (647, 397)],
   [(351, 408), (657, 587)],
   [(383, 590), (692, 771)],
   [(155, 277), (329, 567)],
   [(183, 599), (346, 767)],
    ]),
    ("shelf_images/IMG-20240206-WA0012.jpg", [
    [(130, 231), (301, 349)],
[(104, 355), (288, 478)],
[(341, 296), (456, 391)],
[(338, 401), (449, 496)],
[(322, 604), (445, 704)],
[(456, 504), (598, 605)],
[(459, 402), (597, 496)],
[(473, 297), (609, 395)],
[(606, 417), (735, 501)],
  [(603, 509), (732, 599)],
  [(615, 608), (742, 701)],
  [(614, 706), (739, 783)],
  [(756, 275), (882, 403)],
  [(741, 405), (877, 505)],
  [(742, 507), (873, 604)],
  [(746, 608), (875, 699)],
  [(744, 701), (874, 789)],
  [(913, 264), (1041, 369)],
  [(889, 371), (1014, 486)],
  [(875, 484), (1017, 592)],
  [(879, 601), (1003, 691)],
  [(880, 701), (1006, 779)],
  [(1050, 315), (1172, 404)],
  [(1021, 408), (1149, 505)],
  [(1021, 509), (1143, 595)],
  [(1021, 602), (1146, 699)],
  [(1012, 701), (1145, 786)],
  [(1174, 294), (1292, 392)],
  [(1162, 414), (1295, 540)],
  [(1173, 543), (1311, 671)],
  [(1184, 680), (1326, 787)],
  [(328, 706), (454, 786)],
  [(470, 618), (586, 717)],
  [(459, 722), (604, 784)],
  [(341, 496), (458, 595)],
  [(95, 487), (249, 604)],
  [(107, 611), (265, 727)],
  [(102, 734), (264, 800)],
  [(620, 315), (727, 415)],
        # Add more bounding boxes for Image 3
    ]),
    ("shelf_images/IMG-20240206-WA0013.jpg", [
         [(435, 391), (620, 569)],
   [(356, 594), (512, 780)],
   [(685, 455), (922, 615)],
   [(652, 268), (868, 421)],
   [(707, 637), (951, 802)],
   [(772, 93), (869, 277)],
   [(865, 96), (956, 329)],
   [(1032, 498), (1229, 747)],
   [(116, 414), (245, 691)],
   [(163, 198), (261, 305)],
   [(275, 204), (376, 310)],
    ]),
    ("shelf_images/IMG-20240206-WA0015.jpg", [
         [(559, 266), (699, 582)],
   [(697, 363), (859, 580)],
   [(863, 386), (988, 584)],
   [(990, 384), (1124, 587)],
   [(1129, 386), (1264, 588)],
   [(233, 261), (417, 577)],
   [(184, 628), (355, 750)],
   [(476, 294), (543, 586)],
    ]),
    ("shelf_images/IMG-20240206-WA0016.jpg", [
         [(265, 355), (427, 731)],
   [(414, 260), (628, 722)],
   [(642, 255), (830, 777)],
   [(841, 246), (1039, 728)],
   [(1055, 239), (1285, 731)],
   [(17, 362), (245, 756)],
   [(336, 53), (618, 210)],
   [(634, 96), (864, 163)],
   [(625, 162), (861, 224)],
    ]),
    # Add more images and bounding boxes as needed
]

# Function to create annotated images with bounding boxes
def annotate_images(image_data):
    for image_path, bounding_boxes in image_data:
        # Load the image
        image = cv2.imread(image_path)

        # Draw bounding boxes on the image
        for bbox in bounding_boxes:
            cv2.rectangle(image, bbox[0], bbox[1], (0, 255, 0), 2)

        # Save the annotated image
        annotated_image_path = image_path.replace(".jpg", "_annotated.jpg")
        cv2.imwrite(annotated_image_path, image)

# Call the function to annotate images
annotate_images(image_data)
