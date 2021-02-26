# Meeting Minutes:


Teams present: 
 * Bit-Bots
 * HULKs
 * Dutch Nao Team
 * Boldhearts
 * Naoth
 * Naova
 * NUBots
 * B-Human
 * Bembelbots
 * 01\. RFC Berlin
 * ICHIRO


## Welcome from Pascal

## Presentations of Current Solutions and Requirements

Each team is asked to present the solution they are currently using, the requirements it fulfills, which requirements they might have in the future and the problems they see with the current solution.

### Bit-Bots

Current tool: https://imagetagger.bit-bots.de
#### Features:
* Web app
* different label types (i.e. bounding boxes, lines, multi-lines, polygons, no segmentation)
* multiple public and private imagesets organized in teams
* workflows:
	* labeling view for drawing annotations
	* verification view for verifying annotations of:
		* machine genereated annotations
		* other peoples annotation
* online tool allows for collaboration and sharing

#### Problems
* hard to correct annotations from verification workflow
* bad overview of imagesets

### NU-Bots

* NUpbr: https://nubook.nubots.net/system/tools/nupbr
    * blender to create training images
    * high dynamic range (HDR) background images, lighting conditions also from robocups
    * generate segmentation instead of bounding boxes
    * future work: depth images
    * More robot models are needed
* required metadata: camera info and camera pose relative to robot (intrinsic and extrinsic camera calibration)
* Requirements: 
	* various color spaces
	* stereo input data
	* semantic segmentation can be converted to bounding boxes


### 01 RFC-Berlin

* New team, so no tool

* Requirements 
	* Camera position to replicate situation (metadata)
	* everything in the Bit-Bots Imagetagger (probably annotation, verification)


### BHuman

* write one tool per task they want to do

* Requirements:
	* extract images from their log format
	* bounding boxes and circles (automatically generated)


### Bembelbots

* unreal engine for data generation (SPL)
* real world data annotation with custom tool to draw bounding boxes or polygons for segmentation
* Problems: 
	* time consuming and they dont like that
	* relabeling what previously was background is now robot; label robot parts

### Bold Hearts

no tool yet and no requirements collected


### Dutch Nao Team

* specific handwritten tools for each applications
	* first collect balls using current detector
	* large network to create annotations and small network on robot -> only manually label discrepancies

Requirements: 
* semantic segmentations would be nice for the future
* merge labels from different classification systems (small and large network) and manually label/fix differences (with classification, not annotation)


### HULKs

also use the information from area manually labeled as false positive to improve network; dataset is also used for training of dataset annotation network

Workflow:
* import raw data with special color spaces (ycbcr instead of rgb)
* automatic labeling
* manual cleaning (remove wrong annotations from previous step)
	* false positive remover (shows image areas, click to mark as false positive)
	* true positive adder (= manual annotation)
	* position corrector (used to correct circular annotations by dragging in onto the image)
* export to specific format

UI Requirements:
* minimum clicks/time
* fast switching between views
* focus: only show samples (not whole image)
* hosted web application (desktop + mobile)

Backend Requirements:
* dataset versioning, specific version used in code (https://dvc.org)


### Naoth

use https://cvat.org/
Requirements fulfilled by this software:
* synchronize annotations with github repository
* bounding boxes and semantic segmentation
* reviewer is saved
* 3d bounding boxes (not yet used but interested)
* circular annotations
* automatic annotation with model hosted in docker container (detecton framework)

Generally very satisfied with this tool

### Nao Devils

Same as Naoth

### Naova

no requirements collected yet, no tools



## Completions

After each team has presented, everybody is asked to complete their requirements with things that came in mind during the presentations. In the meeting minutes, these are integrated into each teams section


## Survey

A small survey was prepared during a break. From each team only one person was supposed to answer but we can not verify it. Numerical results of the survey are in the `.csv` file.

Each subsection refers to one or multiple questions as given in the title.



### Label formats (Q1-Q4)
* bounding boxes is definitely required
* segmentation is not used by many teams yet but is interesting in the future
	* a tool for this might enable more research in the direction
* polygons, lines, multi-lines are not as essential as bounding boxes but also very needed
* NUBots represent their labels in different formats than most teams since they do their computer vision in 3D https://www.youtube.com/watch?v=FhJwdtnVusY

### Labeling Process (Q5)
Characteristics of a simple fast and intuitive tool:
* optimize for fewer clicks/less time
* reduce cognitive load
* keyboard input/shortcuts
* touch support might be useful
* see more images at the same time instead for certain tasks
* "magic wand" tool for segmentation
* modify existing labels should be straight forward


### Metadata (Q6)
Three types of metadata:
* Metadata of imagesets
	* indoor/outdoor
	* synthetic image
	* place (e.g. RoboCup 2019)
* Metadata of images
	* camera intrinsics (might be metadata of imageset)
	* camera extrinsics (pose of camera relative to ground or even field center)
	* lens parameters
	* timestamp
* Metadata of annotations
	* blurred
	* concealed
	* background/foreground label (balls on other fields in background)
	* verified
	* automatically or manually labeled, which algorithm was used to generate it
	* was is a false negative/false positive
	* soft labels (percentages 0-1)

General Requirements:
* ability to bisect dataset by metadata
* freely choosable tags which can be merged and filtered


### Color spaces (Q7)
* Currently used colorspaces: RGGB, YCbCr, Grayscale, RGB, YUV, bayer
* Display in RGB, but internal store in original color spaces (prevents loss)
* Nubots convert images between color spaces "on the fly" using webgl
* exportable in other color spaces

### Collaboration (Q8)
* i.e. label with multiple people
* some teams simply use a list for assigning datasets to people (e.g. etherpad/google doc)
* Job system in a tool to divide image set in n jobs or split every m images
* Mode to allow arbitrary number of labelers: show "random" (i.e. not labeled of not many labels) images
	* ability to show (time-)context (in case of uncertain occurencies)


### Data sharing (Q9)
* sharing of final datasets is generally regarded as good
* upload/download via FTB was not very usable
* examples of openly available datasets:
	*  https://sibylle.informatik.uni-bremen.de/public/datasets/
	*  https://logs.naoth.de/
	*  https://imagetagger.bit-bots.de (login required)


### Dataset Management (Q10-Q11)
* metadata to filter/sort/query
* comments to the datasets for arbitrary text
	* could be convenient to have a feedback (is this dataset useful?) or comment section
	* also interesting for single images to

DVC (https://dvc.org)
* needed by some teams, could be more interesting in the future for other teams since it seems to become an industry standard


### Verification (Q12)
TODO!!!!
* if only one person labels a set, there can be a lot of errors
* get an overview of all annotations to verify
* etc, many different use cases
* find false negatives/missing labels, e.g. in time series
* full image view with all labels that can be verified at once (is faster) or point out problems
* two workflows identified: verify as good or bad and fix bad labels afterwards vs. verify or fix immediately
* assign label tag for manually corrected labels (see metadata)


### Import formats (Q13)
* a team should be able to write modules for import/export (or a local solution)
* one standard format often does not work to represent all use cases

### Hosted Web App (Q14)
* pro:
	* OS independent
	* easier for collaboration and sharing
	* a lot of people already have web dev skills
	* no downloads necessary
* contra: 
	* setup should not be too complicated
	* offline work would be nice
	* privacy reasons
* central data store for collaboration is necessary
* labeling could happen offline, online could just compare labels
* before uploading: somehow legally assure the rights

### Automatic Annotation in the "Cloud" (Q15)
* most don't need it, nice to have
* workflow is covered with download -> generate labels -> upload
* it needlessly complicates things

### Fast switch between verification and editing view (Q16)
* depends on verification workflow, is only necessary for verify with immediate editing
* customize views to adapt to own workflow
* or edit and verify are on the same view? 
	* might be less intuitive since there are more buttons on the interface

### Highlighting false positives / false negatives (Q17)
* highlight not necessary, just remember the false positive/negative label to later improve the network
* can be used in feedback for training
* could be implemented as metadata for labels (see metadata)


### Webhooks and API (Q18)
If a tool is a web app, the following webhooks might be useful:
* new datasets
* updated labels
* manual triggering of webhook (instead of after every change)
* "subscribe" to datasets for relevant changes

The API should cover the following requirements:
* everything on the web site should be in the API
* REST APIs are query based, special requests could be used for subscriptions


### Synthetic data (Q19)
Synthetic data can be easily identified using metadata tags (of the imageset).


### Stereo Images (Q20)
* not used by most teams
* images and their labels are linked as a pair would be sufficient

### Export Formats (Q21)
* manually specified annotation output formats (json, xml, ... and yolo darknet) are generally good
* if an output format has unneeded data, it can just be ignored
* a standard format could be used that everyone can converted
	* TFRecord could be the solution
	* hdf5 is also used
* must support different types of annotations
* png with embedded annotations and metadata may also be required
* download annotations and images together, e.g. in a tar ball


### Versioning (with or without git) (Q22-23)
* fixed versions enable repeatablity and comparison and is therefore desirable
* versioning should be possible, git is mostly not needed (as it is not that suited)
* DVC
* how to version
	- every change increases the version
	- or manually after a labeling session
* semantic versioning (semvar) (major-minor-patch versions that are manually increased)
	* or revision numbers
* view differences between versions might be useful

### Labeling jobs (who, which images, which labels) (Q24)
* Assigning the dataset to persons is not always desired, but choosing a labeling job is good
* This task may not belong to the image annotation tool

### Show who labeled / verified what (Q25)
Showing who labeled or verified an annotation might be useful for
* managing annotations (exclude all annotations created by some person or algorithm)
* reward team members for doing lots of labeling
* split labels by who trained them to see which network gets the best accuracy

### Relabeling/Editing (Q26)
* Editing existing labels should be possible
* already talked about in verification

### Merging of labels from different classification systems (Q27)
* Two networks classify images, only differences get shown to the user
* Dutch Nao Team used it for classification, not for object detection (i.e. no pixel problems)
* „Conflict Resolution System“ to select which label is good enough

### Conversion between annotation types (Q28)
* is currently not needed, but relatively easy to implement for some conversions
	* others are really hard or impossible

## Final Discussion
Tools for simple classifification (e.g. is this image a ball) should be handled in a different mode
    - labeling for classification is solved with the annotations, but is probably faster in a different mode


## Goodbye and Thank you

We would like to thank all participants for their contributions and the productive discussion.


