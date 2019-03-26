# Apollo
Apollo is an open source, real-time polling application akin to platforms such as Poll Everywhere and Survey Monkey. It uses Django Channels for to add websocket support to Django and Redis as the websocket channel layer.
The end goal is to have a reliable, easy to setup web application that can be installed on a Raspberry Pi and will serve as a viable alternative to the paid services mentioned, particularly in academic and corporate environments.

At this time Apollo's functionality is limited to:
* Starting either a multiple choice, binary (yes/no), or numeric poll
* viewing responses in real-time in a bar graph or pie chart
* exporting and downloading the results in CSV format

TODO:
* Add login functionality
* implement the private and anonymous poll options
* implement the poll history page
* implement the recent polls column
