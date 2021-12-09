<!-- logo -->
<!-- <p align="center">
  <img width="300" src="logo.png">
</p> -->

<!-- short description -->
<h1 align="center">Eek Anderson Media - Webapp</h1>

<p align="center">
    <!-- code size  -->
    <img src="https://img.shields.io/github/languages/code-size/GSPuniani/eek-anderson-media" />
    <!-- issues -->
    <img src="https://img.shields.io/github/issues/GSPuniani/eek-anderson-media" />
    <!-- pull requests -->
    <img src="https://img.shields.io/github/issues-pr/GSPuniani/eek-anderson-media" />
    <!-- number of commits per year -->
    <img src="https://img.shields.io/github/commit-activity/y/GSPuniani/eek-anderson-media" />
    <!-- last commit -->
    <img src="https://img.shields.io/github/last-commit/GSPuniani/eek-anderson-media" />
</p>


## Table of Contents

- [About](#about)
- [Deployment](#deployment)
- [Team](#team)
- [Back-end Technology](#back-end-technology)
- [Front-end Technology](#front-end-technology)

## About

This webapp is part of an Industry Collaboration project. The main goal for this project is to import a table of music data and create a database that will have a searchable, filterable UI so that our industry partner can easily search his collection of music. This webapp will also be connected to our industry partner's landing page so that any of his prospective clients can also search his music catalog.


## Deployment

The webapp is live! Visit [here](http://13.52.168.242).

The homepage displays the search bar front and center, with the list of results appearing below. Each song result can be expanded to display additional details, such as Mode, Description, Time Signature, and Sounds Like. The search filters can be adjusted in the side panel on the left: the BPM range is adjusted with a slider, and the other filters (Genre, Instrument, and Mood) each have two lists - one for including in the search (right) and one for excluding from the search (left). 

This project is hosted on AWS EC2 with the song database stored in AWS RDS. Our industry partner has access to a simple admin panel so that he can add and update his song catalog with ease.


Home page:

<img width="1437" alt="Home Page" src="https://github.com/GSPuniani/eek-anderson-media/blob/main/screenshots/Home%20Page.png?raw=true">
 

## Team

- Tristan Thompson (Product Manager)
- Joseph Cottingham (Back-end Lead)
- Gobind Puniani (Gitmaster)
- Ryan Lee (Design & QA)
- David Cao (Front-end Lead)


## Back-end Technology

This project uses Django for its back-end framework and PostgreSQL for the database. 

## Front-end Technology

This project uses Bootstrap and Jinja 2 templating for its UI.  












