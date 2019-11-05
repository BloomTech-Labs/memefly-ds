README for memegenerator.net dataset

Dataset originally created 05/07/2018
- UPDATED 05/17/2019 (Updated hashes and file size for all entries)
- UPDATED 05/17/2019 (Replaced missing field values with a uniform placeholder value of '-')
- UPDATED 05/17/2019 (Added fields from the memegenerator.net API: Display Name, Upper Text, & Lower Text)
- UPDATED 05/17/2019 (Added data for rows that were missing information)
	- 266 rows had the text "Unable to locate [http://memegenerator.net/instance/XXXXXXXX]" in the Meme Page URL field. This was a result of:
		1) The Meme Page URL being absent from the archive, i.e., it was never captured;
		2) and an error being received when attempting to fetch the live version of the site
	- These rows were updated with the missing information
- UPDATED 12/11/2018 (Added Contact Information section to README)
- UPDATED 11/20/2018 (Added The Anatomy of A Meme & Contributor sections to README)
- UPDATED 11/15/2018 (Added rights statement and field descriptions to README)
- UPDATED 10/04/2018 (Removed file name column)

I. What's Included?

This dataset includes one CSV file:

- memegenerator.csv

The memegenerator.net dataset was generated from content harvested from the Library of Congress's web archive of memegenerator.net: https://www.loc.gov/item/lcwaN0010226/. It describes 57,687 unique Meme Instances derived from Base Meme Images (meme images without text, waiting to be fashioned into Meme Instances). The dataset includes some minimal metadata for these Meme Instances, but does not include the meme image files; however, it does provide links to access their web archive copies within the Library's web archive.

II. The Anatomy of A Meme

The memes from memegenerator.net are created using a particular formula: Base Meme Images are combined with user supplied Alternate Text to create a Meme Instance. Each of these terms are described below.

- Base Meme Image
    - Base Meme Images are the starting point for meme generation. They are the image without text applied.
    - Each Base Meme Image has a particular name associated with it, called the Base Meme Name. For Example, Conspiracy Keanu.
    - To find out more about Base Meme Names, checkout another archive: Know Your Meme, https://www.loc.gov/item/lcwaN0009692/.
- Alternate Text
    - Alternate Text is the user supplied text that is placed on top of the Base Meme Image. For Example, if the Base Meme Image was of Conspiracy Keanu the Alternate Text might be: What If Carly Rae Jepsen's Real Name Is May Be?
- Meme Instance
    - A Meme Instance is the resulting combination of a Base Meme Image and user supplied Alternate Text. 

III. memegenerator.net Dataset Field Descriptions

- Meme ID: the unique identifier created by memegenerator.net for a Meme Instance.
- Archived URL: a link to the first capture of the image file for a Meme Instance.
    - The archived URL is comprised of four parts:
        1. the web archive domain, webarchive.loc.gov
        2. the access point, all
        3. the date range--a wildcard character of * is used to bring up all captures and in this instance, 0 is a shortcut for the first capture
        4. the resource URL, http://cdn.meme.am/instances/250x250/10698210.jpg
    - More about the Wayback Machine and the URL construction can be found here: https://github.com/iipc/openwayback/wiki/OpenWayback-Replay-API
- Base Meme Name: this is the generic name for a particular meme. e.g., Bad Luck Brian. There are some entries in which a Base Meme Name could not be determined. In these instances, a placeholder value of '-' is used to signify this absence.
- Meme Page URL: a URL to the Meme Instance's web page as opposed to the Archived URL, which points only to the image file. The Meme Page URL points to the "landing page" of the particular Meme Instance. Where available, the URL points to the Library's archived copy. However, for some Meme Instances, we have not captured the "landing page," but only the image file. In these cases, a URL to the live site is provided. There are some entries in which a Meme Page URL could not be determined. In these instances, a placeholder value of '-' is used to signify this absence.
- MD5 Hash: MD5 hash of the of the Meme Instance's image file
- File Size (In Bytes): size of the Meme Instance's image file in bytes
- Alternate Text: the user supplied text that is combined with the Base Meme Image to create the Meme Instance. There are some entries in which Alternate Text could not be determined. In these instances, a placeholder value of '-' is used to signify this absence.
- Display Name: This field is derived from the memegenerator.net API. In most cases, it is analogous to the Base Meme Name. In some instances, however, there may be some variance. There are some entries in which a Display Name could not be determined. In these instances, a placeholder value of '-' is used to signify this absence.
- Upper Text: This field is derived from the memegenerator.net API. As its name implies, it is the upper text featured on a Meme Instance. In most cases, it is analogous to the Alternate Text when combined with the Lower Text. There are some entries in which Upper Text could not be determined. In these instances, a placeholder value of '-' is used to signify this absence.
- Lower Text: This field is derived from the memegenerator.net API. As its name implies, it is the lower text featured on a Meme Instance. In most cases, it is analogous to the Alternate Text when combined with the Upper Text. There are some entries in which Lower Text could not be determined. In these instances, a placeholder value of '-' is used to signify this absence.

IV. Rights Statement

This data set was derived from content in the Library’s web archives. See https://www.loc.gov/item/lcwaN0010226/ for the descriptive record for the source archived web site. The Library follows a notification and permission process in the acquisition of content for the web archives, and to allow researcher access to the archived content, as described on the web archiving program page, https://www.loc.gov/programs/web-archiving/about-this-program/. See also the Rights & Access statement, https://www.loc.gov/collections/web-cultures-web-archive/about-this-collection/rights-and-access/, for the Web Cultures Web Archive for more information.

V. Creator and Contributor Information

Created by Chase Dooley, Digital Collections Specialist, Digital Content Management Section, Library of Congress.

Contributors include:
Trevor Owens, Head, Digital Content Management Section, Library of Congress.
Jesse Johnston, Digital Collections Specialist, Digital Content Management Section, Library of Congress.
Aly DesRochers, Digital Collections Specialist, Digital Content Management Section, Library of Congress.

VI. Contact Information
Please direct all questions and comments to webcapture@loc.gov.