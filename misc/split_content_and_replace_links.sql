# Insert data to table
use training;
set @html_body = "<!doctype html>
<html>
<head>
    <link rel=\"shortcut icon\" href=\"http://cdn.skilledup.com/public/images/icons/SkilledUp-favicon.ico\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0,user-scalable=1.0,minimum-scale=1.0,maximum-scale=1.0\">
        <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/public/css/common.css?f89bcbcf\" />
        <link href='http://fonts.googleapis.com/css?family=Roboto:400,400italic,500,500italic,700,700italic,300,300italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:400,300,700' rel='stylesheet' type='text/css'>
    <link rel=\"stylesheet\" href=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/smoothness/jquery-ui.css\" />
    <meta charset=\"UTF-8\">
    <meta name=\"description\" content=\"Discover the best courses and latest trends in Data Science.description: By 2015, analysts predict that data science careers will increase by 4.4 million.\">
    <title>Learn Data Science | SkilledUp</title>
";
insert ignore into html_content(id, content)
values
(1, @html_body);

# get the value form table
set @original_html = (select content from html_content where id = 1);

# split the html string to two equal parts.
set @html_first = substring(@original_html, 1, char_length(@original_html)/2);
set @html_second = substring(@original_html, (char_length(@original_html)/2)+1, char_length(@original_html));

# TODO: Get the substring that matches the URL pattern
set @url_list = "yet to find a  way";

# TODO: Loop throught the url list and replace the URL text with target

set @target_url = "http://www.google.com";  
set @replaced = replace (@html_first, @url, @target_url);
# create the final content
set @final_content =  concat(@replaced, @html_second);
# update the final content to table
update html_content set content = @final_content where id = 1;
