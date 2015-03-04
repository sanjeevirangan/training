# coding=utf-8
import re


file_content = '''
<!doctype html>
<html>
<head>
    <link rel="shortcut icon" href="http://cdn.skilledup.com/public/images/icons/SkilledUp-favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=1.0,minimum-scale=1.0,maximum-scale=1.0">

        <link rel="stylesheet" type="text/css" href="/static/public/css/common.css?f89bcbcf" />
        <link href='http://fonts.googleapis.com/css?family=Roboto:400,400italic,500,500italic,700,700italic,300,300italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:400,300,700' rel='stylesheet' type='text/css'>

    <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/smoothness/jquery-ui.css" />
    <meta charset="UTF-8">
    <meta name="description" content="Discover the best courses and latest trends in Data Science.description: By 2015, analysts predict that data science careers will increase by 4.4 million.">



    <title>Learn Data Science | SkilledUp</title>

<script type="text/javascript">
csrftoken='';(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','__gaTracker');
__gaTracker('create', 'UA-31013621-6', 'auto');
__gaTracker('require', 'displayfeatures');
__gaTracker('send', 'pageview');
</script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
<script src="//cdn.optimizely.com/js/1863170302.js"></script>
</head>
<body>
<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5J4N8S"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5J4N8S');</script>
<!-- End Google Tag Manager -->
<header>


<nav class="skilledup-nav text-right">
<a href="/">
    <div style="margin-top: 10px;" class="Sprite-SkilledUp-Logo-Primary nav-logo hide-for-medium-down"></div>
    <span class="nav-logo-mobile hide-for-medium-up nav-logo Sprite-SkilledUp-Logo-No-Text"></span>
    <span class="Sprite-SkilledUp-Logo-Primary nav-logo-mobile hide-for-large-up nav-logo hide-for-small-only"></span>
</a>
<ul class="nav-topics-container">
    <li class="nav-tab nav-topics" navtype="topics">
        Topics
        <div class="nav-down-arrow Sprite-Down-Arrow-Black"></div>
        <div class="nav-down-arrow Sprite-Down-Arrow-White"></div>
        <div class="nav-down-arrow Sprite-Up-Arrow-White"></div>
    </li>
    <li class="nav-tab nav-courses" navtype="courses" onclick="window.location.href='/courses'">
        Courses
    </li>
    <li class="nav-tab nav-about" navtype="about">
        About
        <div class="nav-down-arrow Sprite-Down-Arrow-Black"></div>
        <div class="nav-down-arrow Sprite-Down-Arrow-White"></div>
        <div class="nav-down-arrow Sprite-Up-Arrow-White"></div>
    </li>
    <li class="nav-tab nav-signup" navtype="active-signup">
        Sign Up
        <div class="nav-down-arrow Sprite-Down-Arrow-Black"></div>
        <div class="nav-down-arrow Sprite-Down-Arrow-White"></div>
        <div class="nav-down-arrow Sprite-Up-Arrow-White"></div>
    </li>
    <li class="nav-tab nav-login" navtype="active-login">
        Login
        <div class="nav-down-arrow Sprite-Down-Arrow-Black"></div>
        <div class="nav-down-arrow Sprite-Down-Arrow-White"></div>
        <div class="nav-down-arrow Sprite-Up-Arrow-White"></div>
    </li>
    <li class="nav-tab nav-logged-in col-login large" navtype="logged" style="display:none">
      <span class="user-avatar small clickable">
      </span>
      <span class="user-info" rev="logged-in">
          <span class="user-name clickable"></span>
          <div class="nav-down-arrow Sprite-Down-Arrow-Black"></div>
          <div class="nav-down-arrow Sprite-Down-Arrow-White"></div>
          <div class="nav-down-arrow Sprite-Up-Arrow-White"></div>
      </span>
        <div class="hide-for-medium-up">
            <div class="nav-down-arrow Sprite-Down-Arrow-Black"></div>
            <div class="nav-down-arrow Sprite-Down-Arrow-White"></div>
            <div class="nav-down-arrow Sprite-Up-Arrow-White"></div>
        </div>
        <!--<a onclick="window.location = root_url + 'logout?_=' + new Date().getTime()"><span class="icon setting-gray"></span> Log Out</a>-->
    </li>
    <li class="nav-tab nav-toggle" navtype="toggle">
        <div class="Sprite-Nav-Toggle"></div>
        <div class="Sprite-Nav-Toggle-Active"></div>
    </li>
    <li class="nav-tab nav-search" navtype="search">
        <div class="Sprite-Search-Gray"></div>
        <div class="Sprite-Search-White"></div>
    </li>

</ul>

<div class="nav-body nav-topics-dropdown text-center not-320" navtype="topics">


    <div class="large-3 columns nav-pane-1 nav-pane">
        <a href="#" class="hide-for-medium-down">


            <img width="131" height='204' src="http://cdn.skilledup.com/public/images/topics/Topics-Nav-Creative-Character-2x.png"




            <br class="hide-for-medium-down">
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <p class="title">Creative</p>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
        <div class="title  hide-for-large-up">
            <i></i>
            Creative
            <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
            <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
        </div>
        <div class="tile-topics nav-pane-topics">

            <h3><a href="/topics/web-mobile-design">Web &amp; Mobile Design</a></h3>

            <h3><a href="/topics/graphic-design">Graphic Design</a></h3>

            <h3><a href="/topics/photography">Photography</a></h3>

            <h3><a href="/topics/writing-content">Writing &amp; Content</a></h3>

            <h3><a href="/topics/audio-video">Audio &amp; Video</a></h3>

        </div>
    </div>




    <div class="large-3 columns nav-pane-2 nav-pane">
        <a href="#" class="hide-for-medium-down">


            <img width="131" height='204' src="http://cdn.skilledup.com/public/images/topics/Topics-Nav-Technology-Character-2x.png"




            <br class="hide-for-medium-down">
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <p class="title">Technology</p>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
        <div class="title  hide-for-large-up">
            <i></i>
            Technology
            <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
            <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
        </div>
        <div class="tile-topics nav-pane-topics">

            <h3><a href="/topics/data-science">Data Science</a></h3>

            <h3><a href="/topics/engineering">Engineering</a></h3>

            <h3><a href="/topics/information-security">Information Security</a></h3>

            <h3><a href="/topics/cloud-computing">Cloud Computing</a></h3>

            <h3><a href="/topics/computer-networking">Computer Networking</a></h3>

            <h3><a href="/topics/software-development">Software Development</a></h3>

        </div>
    </div>




    <div class="large-3 columns nav-pane-3 nav-pane">
        <a href="#" class="hide-for-medium-down">


            <img width="131" height='204' src="http://cdn.skilledup.com/public/images/topics/Topics-Nav-General-Character-2x.png"




            <br class="hide-for-medium-down">
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <p class="title">General Education</p>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
        <div class="title  hide-for-large-up">
            <i></i>
            General Education
            <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
            <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
        </div>
        <div class="tile-topics nav-pane-topics">

            <h3><a href="/topics/natural-sciences">Natural Sciences</a></h3>

            <h3><a href="/topics/healthcare-life-sciences">Healthcare &amp; Life Sciences</a></h3>

            <h3><a href="/topics/personal-development">Personal Development</a></h3>

            <h3><a href="/topics/humanities">Humanities</a></h3>

            <h3><a href="/topics/foreign-language">Foreign Language</a></h3>

        </div>
    </div>




    <div class="large-3 columns nav-pane-4 nav-pane">
        <a href="#" class="hide-for-medium-down">


            <img width="131" height='204' src="http://cdn.skilledup.com/public/images/topics/Topics-Nav-Business-Character-2x.png"




            <br class="hide-for-medium-down">
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <p class="title">Business</p>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
        <div class="title  hide-for-large-up">
            <i></i>
            Business
            <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
            <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
        </div>
        <div class="tile-topics nav-pane-topics">

            <h3><a href="/topics/business-management">Business &amp; Management</a></h3>

            <h3><a href="/topics/marketing">Marketing</a></h3>

            <h3><a href="/topics/project-management">Project Management</a></h3>

            <h3><a href="/topics/sales">Sales</a></h3>

            <h3><a href="/topics/business-law">Business Law</a></h3>

            <h3><a href="/topics/accounting-finance">Accounting &amp; Finance</a></h3>

        </div>
    </div>



</div>

<div class="nav-body nav-about-dropdown text-center not-320" navtype="about">
    <div class="large-4 medium-4 small-12 columns">
        <a href="/about/">
            <div class="Sprite-Our-Story-Icon icon"></div><br class="hide-for-small-only" />
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <div class="title">Our Story</div>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
    </div>
    <div class="large-4 medium-4 small-12 columns">

        <a href="http://skilledup.zendesk.com/" target="_blank">
            <div class="Sprite-Help-Center-Icon icon"></div><br class="hide-for-small-only" />
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <div class="title">Help Center</div>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
    </div>
    <div class="large-4 medium-4 small-12 columns">

        <a href="/insights">
            <div class="Sprite-Trends-Insights-Icon icon"></div><br class="hide-for-small-only" />
            <div class="tile-title-top-border-left white-bg v-bottom"></div>
            <div class="tile-title-top-border-right white-bg v-bottom"></div>
            <div class="title">Trends &amp; Insights</div>
            <div class="tile-title-top-border-right white-bg"></div>
            <div class="tile-title-top-border-left white-bg"></div>
        </a>
    </div>
</div>

<div class="nav-body mobile-dropdown not-320" navtype="active-signup">
    <div class="collapsable-tab tab-signup hide-for-medium-up">
        Sign Up
        <div class="Sprite-Down-Arrow-White arrow"></div>
        <div class="Sprite-Up-Arrow-White arrow"></div>
    </div>
    <div class="nav-signup-dropdown">
        <div class="row text-center">
            <div class="large-12 columns large-centered hide-for-small-only">
                <p>Start Learning</p>
                <div class="tile-title-top-border-left white-bg"></div>
                <h3>Sign Up</h3>
            </div>
        </div>

        <div class="row social-login-row">
            <div class="nav-login-header text-left">Sign up with social media</div>
            <div class="large-4 medium-4 small-4 columns">
                <div class="expand nav-social-button button" onclick="window.location='/login/linkedin-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="linked-social-img"></div></div>
            </div>
            <div class="large-4 medium-4 small-4 columns">
                <div class="expand facebook-button button" onclick="window.location='/login/facebook-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="facebook-social-img"></div></div>
            </div>
            <div class="large-4 medium-4 small-4 columns">
                <div class="expand google-plus-button button" onclick="window.location='/login/google-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="google-social-img"></div></div>
            </div>
        </div>
        <div class="row">
            <div class="nav-login-header text-left">Sign up with your email address</div>
            <div class="form-input" rev='registration'>

                <div class="large-8 medium-8 small-12 columns nav-signup-block">
                    <div class="row">
                        <div class="large-6 medium-6 small-12 columns login-input-field">
                            <input type="text" name="first_name" class="nav-input-field margin-bottom-10 nav-name-input" placeholder="First Name" required="required" src="" />
                        </div>

                        <div class="large-6 medium-6 small-12 columns login-input-field">
                            <input type="text" name="last_name" class="nav-input-field margin-bottom-10 nav-name-input" placeholder="Last Name" required="required" src="" />
                        </div>
                    </div>

                    <div class="row">
                        <div class="large-6 medium-6 small-12 columns login-input-field">
                            <input type="email" name="email" class="nav-input-field nav-email-signup margin-bottom-10" placeholder="Email Address" required="required" src="" />
                        </div>

                        <div class="large-6 medium-6 small-12 columns login-input-field">
                            <input type="email" name="confirm_email" class="nav-input-field nav-email-signup-confirm margin-bottom-10" placeholder="Confirm Email Address" required="required" src="" />
                        </div>
                    </div>

                    <div class="row">
                        <div class="large-6 medium-6 small-12 columns login-input-field">
                            <input type="password" name="password" class="margin-bottom-10 nav-input-field nav-signup-password" placeholder="Password (minimum 8 characters)" required="required">
                        </div>

                        <div class="large-6 medium-6 small-12 columns login-input-field">
                            <input type="password" name="confirm_password" class="nav-input-field nav-signup-password-confirm"placeholder="Confirm Password" required="required">
                        </div>
                    </div>
                </div>


                <div class="large-4 medium-4 small-12 columns">
                    <div class="button expand nav-signup-button black-button">Sign Up</div>
                </div>


            </div>
        </div>

    </div><!-- div.nav-signup-dropdown -->
    <div class="collapsable-tab tab-login hide-for-medium-up">
        Login
        <div class="Sprite-Down-Arrow-White arrow"></div>
        <div class="Sprite-Up-Arrow-White arrow"></div>
    </div>
    <div class="nav-login-dropdown">
        <div class="row text-center">
            <div class="large-12 columns large-centered hide-for-small-only">
                <p>Welcome Back!</p>
                <div class="tile-title-top-border-left white-bg"></div>
                <h3>Log In</h3>
            </div>
        </div>
        <div class="row social-login-row">
            <div class="nav-login-header text-left">Log in with social media</div>
            <div class="large-4 medium-4 small-4 columns">
                <div class="expand nav-social-button button" onclick="window.location='/login/linkedin-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="linked-social-img"></div></div>
            </div>
            <div class="large-4 medium-4 small-4 columns">
                <div class="expand facebook-button button" onclick="window.location='/login/facebook-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="facebook-social-img"></div></div>
            </div>
            <div class="large-4 medium-4 small-4 columns">
                <div class="expand google-plus-button button" onclick="window.location='/login/google-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="google-social-img"></div></div>
            </div>
        </div>

        <div class="row login-email-password">
            <div class="nav-login-header text-left">Log in with your email address</div>
            <div class="form-input" rev="login">

                <div class="large-4 medium-4 small-12 columns login-input-field">
                    <input type="text" class="nav-input-field margin-bottom-10 nav-email-input" name="email" placeholder="Email Address"  required="required" src=""/>
                    <div style="width:100%; margin-bottom:60px; text-align:left;"><div class='nav-login-header forgot-email forgot-password' style="float:left; width:105px; padding-left:0px;cursor:pointer;">FORGOT EMAIL?</div></div>
                </div>

                <div class="large-4 medium-4 small-12 columns login-input-field text-left">
                    <input type="password" class="nav-input-field nav-password-input margin-bottom-10" name="password" placeholder="Password" required="required"/>
                    <div style="width:100%; margin-bottom:60px; text-align:left;"><div class='nav-login-header forgot-password' style="float:left; width:130px; padding-left:0px;cursor:pointer;">FORGOT PASSWORD?</div></div>
                 </div>

                <div class="large-4 medium-4 small-12 columns">
                    <div class="button expand login-button-nav login-button-2 black-button" onclick="handleLogin($(this).closest('.form-input'))">Log In</div>
                    <li class="error-message" rel="general"></li>
                </div>

            </div>
        </div>
        <div class="row form-input login-reset-password" style="display:none;">
            <div class="large-4 medium-4 small-12 columns login-input-field text-left" style="display:table">
                <div class="nav-login-header text-left">Enter your email address to reset your password.</div>
            </div>
            <div class="large-4 medium-4 small-12 columns login-input-field text-left" style="margin-bottom:30px">
                <input type="text" class="nav-input-field reset-password-input nav-email-input" name="email" placeholder="Email Address"  required="required" src=""/>
            </div>
            <div class="large-4 medium-4 small-12 columns" style="display:table; margin-bottom:30px;">
                <div class="button expand send-email-button login-button-nav black-button">SEND EMAIL TO RESET</div>
            </div>
        </div>
    </div><!-- div.nav-login-dropdown -->
</div>

<div class="nav-body nav-search-dropdown" navtype="search">
    <div class="row">
        <div class="large-6 columns large-centered text-center">
            <h3>Type Your Search Below</h3>
            <div class="tile-nav-search-border white-bg"></div>
        </div>
    </div>

    <div id="nav-search-container" class="text-center">
        <div class="search-nav-dropdown search-dropdown column small-12 small-centered" value="all">
            <span>ALL</span><div class="select-img"></div>
        </div>
        <input class="search-nav search-input column small-12" type="text" autocomplete="false"/>
        <div class="search-nav-result search-result"></div>
    </div>
</div>

<div class="nav-body nav-logged-in-dropdown" navtype="logged">
    <div class="row">
        <div class="large-9 medium-12 columns large-centered">

            <div class="row hide-for-medium-down">
                <div class="large-4 medium-2 small-2 columns text-right">
                    <span class="user-avatar"></span>
                </div>
                <div class="large-8 medium-10 small-10 columns text-left profile-links-area">
                    <div class="tile-title-top-border-right white-bg short-narrow"></div>
                    <h4 class="user-name"></h4>
                    <div class="row hide-for-medium-down">
                        <div class="large-12 columns">
                            <ul class="nav-user-profile-links">
                                <li><a onclick="loadProfilePage(0)">my saved courses</a></li>
                                <li><a onclick="loadProfilePage(1)">my written reviews</a></li>
                                <li><a onclick="loadProfilePage(3)">my notifications</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="row">
                        <div class="large-6 columns">
                            <a onclick="loadProfilePage(2)"><div id="view-profile" class="button black-button width-all nav-profile-buttons">view profile</div></a>
                        </div>
                        <div class="large-6 columns">
                            <div class="button black-button width-all nav-profile-buttons" onclick="window.location = root_url + 'logout/?_=' + new Date().getTime()">Logout</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row hide-for-large-up nav-sub">
                <div class="medium-12 small-12" onclick="loadProfilePage(2)">
                    <a>
                        <span class="user-avatar"></span>
                        <div class="infor-user">
                            <div class="tile-title-top-border-right white-bg"></div>
                            <h4 class="user-name"></h4>
                        </div>
                    </a>
                </div>
            </div>
            <div class="row hide-for-large-up nav-sub">
                <div class="medium-12 small-12">
                    <a href="#" onclick="loadProfilePage(0)">
                        My Saved Courses
                    </a>
                </div>
            </div>
            <div class="row hide-for-large-up nav-sub">
                <div class="medium-12 small-12">
                    <a href="#" onclick="loadProfilePage(1)">
                        My Written Reviews
                    </a>
                </div>
            </div>
            <div class="row hide-for-large-up nav-sub">
                <div class="medium-12 small-12">
                    <a href="#" onclick="loadProfilePage(3)">
                        My Notifications
                    </a>
                </div>
            </div>
            <div class="row hide-for-large-up">
                <div class="medium-12 small-12">
                    <div class="btn-logout">
                        <a href="/logout">
                            <div class="button black-button width-all">Logout</div>
                        </a>
                    </div>
                </div>
            </div>

        </div>
    </div>

</div>

<div class="dropdown-320 nav-body"  navtype="toggle">
    <div class="list-collapsable">
        <div class="collapsable-tab collapsable-topics" navmobiletype="topics">
            Topics
        </div>
        <div class="collapsable-tab collapsable-about" navmobiletype="about">
            About
        </div>
        <div class="collapsable-tab collapsable-signup" navmobiletype="signup">
            Sign Up
        </div>
        <div class="collapsable-tab collapsable-login" navmobiletype="login">
            Login
        </div>
    </div>
    <div class="list-dropdown">
        <div class="back">Back</div>
        <div class="nav-topics-dropdown text-center drop-general" navmobiletype="topics">


            <div class="large-3 columns nav-pane-1 nav-pane">
                <a href="#" class="hide-for-medium-down">
                    <img width='131'height='204' src="http://cdn.skilledup.com/public/images/nav-topic-placeholder.png" alt="placeholder" class="hide-for-medium-down"><br class="hide-for-medium-down">
                    <div class="tile-title-top-border-left white-bg v-bottom"></div>
                    <div class="tile-title-top-border-right white-bg v-bottom"></div>
                    <p>Creative</p>
                    <div class="tile-title-top-border-right white-bg"></div>
                    <div class="tile-title-top-border-left white-bg"></div>
                </a>
                <div class="title  hide-for-large-up">
                    <i></i>
                    Creative
                    <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
                    <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
                </div>
                <div class="tile-topics nav-pane-topics">

                    <h3><a href="/topics/6">Web &amp; Mobile Design</a></h3>

                    <h3><a href="/topics/10">Graphic Design</a></h3>

                    <h3><a href="/topics/12">Photography</a></h3>

                    <h3><a href="/topics/13">Writing &amp; Content</a></h3>

                    <h3><a href="/topics/14">Audio &amp; Video</a></h3>

                </div>
            </div>




            <div class="large-3 columns nav-pane-2 nav-pane">
                <a href="#" class="hide-for-medium-down">
                    <img width='131'height='204' src="http://cdn.skilledup.com/public/images/nav-topic-placeholder.png" alt="placeholder" class="hide-for-medium-down"><br class="hide-for-medium-down">
                    <div class="tile-title-top-border-left white-bg v-bottom"></div>
                    <div class="tile-title-top-border-right white-bg v-bottom"></div>
                    <p>Technology</p>
                    <div class="tile-title-top-border-right white-bg"></div>
                    <div class="tile-title-top-border-left white-bg"></div>
                </a>
                <div class="title  hide-for-large-up">
                    <i></i>
                    Technology
                    <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
                    <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
                </div>
                <div class="tile-topics nav-pane-topics">

                    <h3><a href="/topics/5">Data Science</a></h3>

                    <h3><a href="/topics/7">Engineering</a></h3>

                    <h3><a href="/topics/8">Information Security</a></h3>

                    <h3><a href="/topics/9">Cloud Computing</a></h3>

                    <h3><a href="/topics/17">Computer Networking</a></h3>

                    <h3><a href="/topics/20">Software Development</a></h3>

                </div>
            </div>




            <div class="large-3 columns nav-pane-3 nav-pane">
                <a href="#" class="hide-for-medium-down">
                    <img width='131'height='204' src="http://cdn.skilledup.com/public/images/nav-topic-placeholder.png" alt="placeholder" class="hide-for-medium-down"><br class="hide-for-medium-down">
                    <div class="tile-title-top-border-left white-bg v-bottom"></div>
                    <div class="tile-title-top-border-right white-bg v-bottom"></div>
                    <p>General Education</p>
                    <div class="tile-title-top-border-right white-bg"></div>
                    <div class="tile-title-top-border-left white-bg"></div>
                </a>
                <div class="title  hide-for-large-up">
                    <i></i>
                    General Education
                    <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
                    <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
                </div>
                <div class="tile-topics nav-pane-topics">

                    <h3><a href="/topics/16">Natural Sciences</a></h3>

                    <h3><a href="/topics/18">Healthcare &amp; Life Sciences</a></h3>

                    <h3><a href="/topics/24">Personal Development</a></h3>

                    <h3><a href="/topics/25">Humanities</a></h3>

                    <h3><a href="/topics/26">Foreign Language</a></h3>

                </div>
            </div>




            <div class="large-3 columns nav-pane-4 nav-pane">
                <a href="#" class="hide-for-medium-down">
                    <img width='131'height='204' src="http://cdn.skilledup.com/public/images/nav-topic-placeholder.png" alt="placeholder" class="hide-for-medium-down"><br class="hide-for-medium-down">
                    <div class="tile-title-top-border-left white-bg v-bottom"></div>
                    <div class="tile-title-top-border-right white-bg v-bottom"></div>
                    <p>Business</p>
                    <div class="tile-title-top-border-right white-bg"></div>
                    <div class="tile-title-top-border-left white-bg"></div>
                </a>
                <div class="title  hide-for-large-up">
                    <i></i>
                    Business
                    <span class="Sprite-Down-Arrow-White arrow hide-for-large-up"></span>
                    <span class="Sprite-Up-Arrow-White arrow hide-for-large-up"></span>
                </div>
                <div class="tile-topics nav-pane-topics">

                    <h3><a href="/topics/11">Business &amp; Management</a></h3>

                    <h3><a href="/topics/15">Marketing</a></h3>

                    <h3><a href="/topics/19">Project Management</a></h3>

                    <h3><a href="/topics/21">Sales</a></h3>

                    <h3><a href="/topics/22">Business Law</a></h3>

                    <h3><a href="/topics/23">Accounting &amp; Finance</a></h3>

                </div>
            </div>



        </div>
        <div class="nav-about-dropdown text-center drop-general" navmobiletype="about">
            <div class="large-4 medium-4 small-12 columns">
                <a href="/about/">
                    <div class="Sprite-Our-Story-Icon icon"></div><br class="hide-for-small-only" />
                    Our Story
                </a>
            </div>
            <div class="large-4 medium-4 small-12 columns">

                <a href="http://skilledup.zendesk.com/">
                    <div class="Sprite-Help-Center-Icon icon"></div><br class="hide-for-small-only" />
                    Help Center
                </a>
            </div>
            <div class="large-4 medium-4 small-12 columns">

                <a href="/insights">
                    <div class="Sprite-Trends-Insights-Icon icon"></div><br class="hide-for-small-only" />
                    Trends &amp; Insights
                </a>
            </div>
        </div>

        <div class="nav-signup-dropdown drop-general" navmobiletype="signup">
            <div class="row text-center">
                <div class="large-12 columns large-centered hide-for-small-only">
                    <h3>Sign In</h3>
                </div>
            </div>

            <div class="row social-login-row">
                <div class="nav-login-header text-left">sign up with a service</div>
                <div class="large-4 medium-4 small-4 columns">
                    <div class="expand nav-social-button button" onclick="window.location='/login/linkedin-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="linked-social-img"></div></div>
                </div>
                <div class="large-4 medium-4 small-4 columns">
                    <div class="expand facebook-button button" onclick="window.location='/login/facebook-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="facebook-social-img"></div></div>
                </div>
                <div class="large-4 medium-4 small-4 columns">
                    <div class="expand google-plus-button button" onclick="window.location='/login/google-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="google-social-img"></div></div>
                </div>
            </div>
            <div class="row">
                <div class="nav-login-header text-left">or sign up by email</div>
                <div class="form-input" rev='registration'>

                    <div class="large-8 medium-8 small-12 columns nav-signup-block">
                        <div class="row">
                            <div class="large-6 medium-6 small-12 columns login-input-field">
                                <input type="text" name="first_name" class="nav-input-field margin-bottom-10 nav-name-input" placeholder="First Name" required="required" src="" />
                            </div>

                            <div class="large-6 medium-6 small-12 columns login-input-field">
                                <input type="text" name="last_name" class="nav-input-field margin-bottom-10 nav-name-input" placeholder="Last Name" required="required" src="" />
                            </div>
                        </div>

                        <div class="row">
                            <div class="large-6 medium-6 small-12 columns login-input-field">
                                <input type="email" name="email" class="nav-input-field nav-email-signup margin-bottom-10" placeholder="Email Address" required="required" src="" />
                            </div>

                            <div class="large-6 medium-6 small-12 columns login-input-field">
                                <input type="email" name="confirm_email" class="nav-input-field nav-email-signup-confirm margin-bottom-10" placeholder="Confirm Email Address" required="required" src="" />
                            </div>
                        </div>

                        <div class="row">
                            <div class="large-6 medium-6 small-12 columns login-input-field">
                                <input type="password" name="password" class="nav-input-field margin-bottom-10 nav-signup-password" placeholder="Password (minimum 8 characters)" required="required">
                            </div>

                            <div class="large-6 medium-6 small-12 columns login-input-field">
                                <input type="password" name="confirm_password" class="nav-input-field nav-signup-password-confirm"placeholder="Confirm Password" required="required">
                            </div>
                        </div>
                    </div>


                    <div class="large-4 medium-4 small-12 columns">
                        <div class="button expand nav-signup-button black-button">Sign Up</div>
                    </div>


                </div>
            </div>

        </div><!-- div.nav-signup-dropdown -->

        <div class="nav-login-dropdown drop-general" navmobiletype="login">
            <div class="row text-center">
                <div class="large-12 columns large-centered hide-for-small-only">
                    <h3>Log In</h3>
                </div>
            </div>
            <div class="row social-login-row">
                <div class="nav-login-header text-left">login with a service</div>
                <div class="large-4 medium-4 small-4 columns">
                    <div class="expand nav-social-button button" onclick="window.location='/login/linkedin-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="linked-social-img"></div></div>
                </div>
                <div class="large-4 medium-4 small-4 columns">
                    <div class="expand facebook-button button" onclick="window.location='/login/facebook-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="facebook-social-img"></div></div>
                </div>
                <div class="large-4 medium-4 small-4 columns">
                    <div class="expand google-plus-button button" onclick="window.location='/login/google-oauth2?_=' + new Date().getTime() + '&next=' + window.location.href"><div class="google-social-img"></div></div>
                </div>
            </div>



                <div class="row login-email-password">
                    <div class="nav-login-header text-left">Log in with your email address</div>
                    <div class="form-input" rev="login">

                        <div class="large-4 medium-4 small-12 columns login-input-field">
                            <input type="text" class="nav-input-field margin-bottom-10 nav-email-input" name="email" placeholder="Email Address"  required="required" src=""/>
                        </div>

                        <div class="large-4 medium-4 small-12 columns login-input-field text-left">
                            <input type="password" class="nav-input-field nav-password-input margin-bottom-10" name="password" placeholder="Password" required="required"/>
                            <div style="width:100%; margin-bottom:60px; text-align:left;"><div class='nav-login-header' style="float:left; width:130px; padding-left:0px">FORGOT PASSWORD?</div><div style="float:left; cursor:pointer; padding-left:0px;" class="nav-login-header forgot-password">RESET</div></div>
                        </div>

                        <div class="large-4 medium-4 small-12 columns">
                            <div class="button expand login-button-nav login-button-2 black-button" onclick="handleLogin($(this).closest('.form-input'))">Log In</div>
                            <li class="error-message" rel="general"></li>
                        </div>

                    </div>
                </div>
                <div class="row form-input login-reset-password" style="display:none;">
                    <div class="large-4 medium-4 small-12 columns login-input-field text-left" style="display:table">
                        <div class="nav-login-header text-left" style="padding-left:0px">Enter your email address to reset your password.</div>
                    </div>
                    <div class="large-4 medium-4 small-12 columns login-input-field text-left" style="margin-bottom:30px">
                        <input type="text" class="nav-input-field reset-password-input nav-email-input" name="email" placeholder="Email Address"  required="required" src=""/>
                    </div>
                    <div class="large-4 medium-4 small-12 columns" style="display:table; margin-bottom:30px;">
                        <div class="button expand send-email-button login-button-nav black-button">SEND EMAIL TO RESET</div>
                    </div>
                </div>






        </div><!-- div.nav-login-dropdown -->
    </div>
</div><!-- div.dropdown-320 -->

</nav>
</header>

<div id="root-container">



<div class="topicSRP" pagetitle="learning-hub-page">







<div class="top-page-header topic-srp">
    <div class="top-page-1 default" style="background-image: url('http://cdn.skilledup.com/public/images/backgrounds/Tech-Environment-Wide.jpg');">


            <div class="topic-breadcrumb">
            </div>

                <div class="topic-label">Topic</div>
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
                <div class="topic-headlight">Data Science</div>


    </div>
    <div class="top-page-2" style='z-index: 10;'>

        <div class="topic-character-wrapper"><div class="topic-character">


                    <img src="http://cdn.skilledup.com/public/images/topics/Character-Data.png" />


        </div></div>

        <ul>
            <li>
                <a href="/courses?topic_ids=5">
                    <div>6,137</div>
                    <div>COURSES</div>
                </a>
            </li>
            <li>
                <a href="/articles?topic_ids=5">
                    <div>50</div>
                    <div>ARTICLES</div>
                </a>
            </li>

            <li>
                <div class="topic-character-wrapper"><div class="topic-character">


                            <img src="http://cdn.skilledup.com/public/images/topics/Character-Data.png" />


                </div></div>
            </li>

            <li>
                <a href="/careers?topic_ids=5">
                    <div>21</div>
                    <div>CAREERS</div>
                </a>
            </li>
            <li>
                <a href="/skills?topic_ids=5">
                    <div>126</div>
                    <div>SKILLS</div>
                </a>
            </li>
        </ul>
    </div>
</div>

    <div class="row ">
        <div class="bx-wrapper slider-top-entities show-for-large-up">
            <div class="bx-slider-container" style="margin-top:50px;">
                <div class="control-list bx-controls-direction">
                    <span id="bxslider-prev-course"></span>

                        <span class="control-list-font">Top Courses</span>

                    <span id="bxslider-next-course"></span>

                </div>
                <a class="button" href="/courses?topic_ids=5">VIEW ALL COURSES</a>
                <ul class="bxslider" rel="course">

                        <li class="large-3 columns">

<a href="/courses/introduction-data-science.110074">
    <div class="course-tile-item course-item" id="110074" providerid="201">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/generalassembly_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Introduction to Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$49 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science.7843">
    <div class="course-tile-item course-item" id="7843" providerid="105">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/edureka_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>


                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>


                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$407 </span>


                </div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-hadoop-visualization.21015">
    <div class="course-tile-item course-item" id="21015" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science from Hadoop to Visualization</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-business-need-know-data-mining-data-analytic-thinking.37227">
    <div class="course-tile-item course-item" id="37227" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science for Business What you need to know about data mining and data-analytic thinking</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$33.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-en-agricultura.107103">
    <div class="course-tile-item course-item" id="107103" providerid="44">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/canvas_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Foreign Language </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science en Agricultura</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">



                        <span class="see-provider-price">See Provider for Price</span>

                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-straight-talk-frontline.37216">
    <div class="course-tile-item course-item" id="37216" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Doing Data Science Straight Talk from the Frontline</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$38.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-concepts-missteps.22117">
    <div class="course-tile-item course-item" id="22117" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science: Concepts and Missteps</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-sidekicks-building-blocks-data-science-workflows.21669">
    <div class="course-tile-item course-item" id="21669" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Sidekicks and Other Building Blocks for Data Science Workflows</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-corporation-live-panel-session.22558">
    <div class="course-tile-item course-item" id="22558" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science and the Corporation: Live Panel Session</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-smart-using-data-science-transform-information-insight.56473">
    <div class="course-tile-item course-item" id="56473" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Smart Using Data Science to Transform Information into Insight</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$45 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-command-line-facing-future-time-tested-tools.43082">
    <div class="course-tile-item course-item" id="43082" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science at the Command Line Facing the Future with Time-Tested Tools</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$33.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/tapping-data-science-create-lasting-customer-relationships.17028">
    <div class="course-tile-item course-item" id="17028" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Tapping Data Science to Create Lasting Customer Relationships</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                </ul>
            </div>
        </div>
        <div class="bx-wrapper slider-top-entities slider-3-slides">
            <div class="bx-slider-container" style="margin-top:60px;">
                <div class="control-list bx-controls-direction">
                    <span id="bxslider-prev-courseTablet"></span>

                        <span class="control-list-font">Top Courses</span>

                    <span id="bxslider-next-courseTablet"></span>

                </div>
                <a class="button" href="/courses?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="courseTablet">

                        <li class="large-3 columns">

<a href="/courses/introduction-data-science.110074">
    <div class="course-tile-item course-item" id="110074" providerid="201">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/generalassembly_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Introduction to Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$49 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science.7843">
    <div class="course-tile-item course-item" id="7843" providerid="105">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/edureka_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>


                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>


                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$407 </span>


                </div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-hadoop-visualization.21015">
    <div class="course-tile-item course-item" id="21015" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science from Hadoop to Visualization</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-business-need-know-data-mining-data-analytic-thinking.37227">
    <div class="course-tile-item course-item" id="37227" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science for Business What you need to know about data mining and data-analytic thinking</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$33.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-en-agricultura.107103">
    <div class="course-tile-item course-item" id="107103" providerid="44">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/canvas_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Foreign Language </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science en Agricultura</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">



                        <span class="see-provider-price">See Provider for Price</span>

                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-straight-talk-frontline.37216">
    <div class="course-tile-item course-item" id="37216" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Doing Data Science Straight Talk from the Frontline</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$38.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-concepts-missteps.22117">
    <div class="course-tile-item course-item" id="22117" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science: Concepts and Missteps</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-sidekicks-building-blocks-data-science-workflows.21669">
    <div class="course-tile-item course-item" id="21669" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Sidekicks and Other Building Blocks for Data Science Workflows</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-corporation-live-panel-session.22558">
    <div class="course-tile-item course-item" id="22558" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science and the Corporation: Live Panel Session</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                </ul>
            </div>
        </div>
        <div class="bx-wrapper slider-top-entities slider-2-slides">
            <div class="bx-slider-container" style="margin-top:60px;">
                <div class="control-list bx-controls-direction">
                    <span id="bxslider-prev-courseTabletPortrait"></span>

                        <span class="control-list-font">Top Courses</span>

                    <span id="bxslider-next-courseTabletPortrait"></span>

                </div>
                <a class="button" href="/courses?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="courseTabletPortrait">

                        <li class="large-3 columns">

<a href="/courses/introduction-data-science.110074">
    <div class="course-tile-item course-item" id="110074" providerid="201">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/generalassembly_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Introduction to Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$49 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science.7843">
    <div class="course-tile-item course-item" id="7843" providerid="105">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/edureka_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>


                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>


                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$407 </span>


                </div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-hadoop-visualization.21015">
    <div class="course-tile-item course-item" id="21015" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science from Hadoop to Visualization</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-business-need-know-data-mining-data-analytic-thinking.37227">
    <div class="course-tile-item course-item" id="37227" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science for Business What you need to know about data mining and data-analytic thinking</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$33.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-en-agricultura.107103">
    <div class="course-tile-item course-item" id="107103" providerid="44">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/canvas_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Foreign Language </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science en Agricultura</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">



                        <span class="see-provider-price">See Provider for Price</span>

                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-straight-talk-frontline.37216">
    <div class="course-tile-item course-item" id="37216" providerid="348">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/oreillymedia_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Doing Data Science Straight Talk from the Frontline</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$38.99 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>



                        <div class="details-text comparison-product-type">book</div>



                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                </ul>
            </div>
        </div>
        <div class="bx-wrapper slider-top-entities show-for-small-only">
            <div class="bx-slider-container" style="margin-top:14px;">
                <div class="control-list bx-controls-direction">
                    <span id="bxslider-prev-courseMobile"></span>

                        <span class="control-list-font">Top Courses</span>

                    <span id="bxslider-next-courseMobile"></span>

                </div>
                <a class="button" href="/courses?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="courseMobile">

                        <li class="large-3 columns">

<a href="/courses/introduction-data-science.110074">
    <div class="course-tile-item course-item" id="110074" providerid="201">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/generalassembly_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Introduction to Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$49 </span>


                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science.7843">
    <div class="course-tile-item course-item" id="7843" providerid="105">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/edureka_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>


                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>



                            <li class="Sprite-Star-Full-Yellow"></li>


                    </ul>
                </div>
                <div class="course-price">


                        <span class="reg-price">$407 </span>


                </div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>

                        <div class="details-text comparison-product-type">course</div>





                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                        <li class="large-3 columns">

<a href="/courses/data-science-hadoop-visualization.21015">
    <div class="course-tile-item course-item" id="21015" providerid="37">

        <div class="course-tile-main">
            <div class="course-provider-icon">
                <img src="http://cdn.skilledup.com/provider-icons/brighttalk_library_icon.png" width="60" height="60" style="max-height: 60px; max-width:60px;" alt="" onerror="this.src='http://cdn.skilledup.com/public/images/Provider-Default-Image-2x.png'">
            </div>
            <span class="item-provider topic-1-color hide-for-small"> Data Science </span>

            <div class="tile-subject-container">
                <div class="tile-header-top-border">
                    <div class="tile-title-top-border-left"></div>
                    <div class="tile-title-top-border-right"></div>
                </div>
                <h3 class="tile-header-subject">Data Science from Hadoop to Visualization</h3>
                <div class="tile-header-bottom-border">
                    <div class="tile-title-bottom-border-left"></div>
                    <div class="tile-title-bottom-border-right"></div>
                </div>
            </div>

            <div class="course-tile-rating-price">
                <div class="star-rating-container">
                    <ul>

                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>
                            <li class="Sprite-Star-Full-Gray"></li>

                    </ul>
                </div>
                <div class="course-price">

                        <span class="reg-price">FREE</span>



                </div>

                    <div class="no-reviews">NO REVIEWS</div>

            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell" style="width:50%">
                    <div class="detail-wrapper">
                        <div  class='footer-mini-item'>
                            <img width='17' height='27' src="http://cdn.skilledup.com/public/images/course-type.jpg" alt="course type">
                        </div>




                        <div class="details-text comparison-product-type">webinar</div>


                    </div>
                </div>
                <div class="table-cell">
                    <div class="detail-wrapper">
                     </div>
                </div>
            </div>
        </div>
    </div>
</a>
                        </li>

                </ul>
            </div>
        </div>
    </div>

    <div class="row">


        <div class="bx-wrapper show-for-large-up">
    <div class="bx-slider-container slider-top-entities">
        <div class="control-list  bx-controls-direction">
            <span id="bxslider-prev-article"></span>

                <span class="control-list-font">Our Trending Articles</span>

            <span id="bxslider-next-article"></span>


        </div>

            <a class="button" href="/articles?topic_ids=5">VIEW ALL ARTICLES</a>

        <ul class="bxslider" rel="article">

            <li class="large-3 columns">
                <a href="/articles/test-drive-college-statistics-major">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Test-Drive-A-College-Statistics-Major-Feature_1290x688_KL-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Test Drive a College Statistics Major
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;08/31/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;8 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/best-mongodb-courses-online-tapping-big-demand-big-data">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/mongoDB-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Best MongoDB Courses Online: Tapping the Big Demand for Big Data Skills
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;07/03/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/5-paid-courses-learning-r-programming">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/paid-R-Program-courses-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    5 Paid Courses for Learning R Programming
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/08/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/41-tech-conferences-developers-data-scientists-engineers">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/02/tech-conferences-­Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    41 Technology Conferences for Developers, Data Scientists, and Engineers
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/03/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learn-google-analytics-with-these-courses">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Google-analytics-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Personal Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learn Google Analytics the Easy Way with these Courses
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;11/12/2012</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learning-sql-is-easy">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/SQL-database-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learning SQL Is An Easy Path to a $92k/Year Career
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/14/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;5 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/python-experts-to-follow">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/Python-experts-websites-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Python Experts to Follow
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/06/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learn-sql-today-make-big-job-market-tomorrow">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/learn-SQL-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learn SQL Today, Make It Big in the Job Market Tomorrow!
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;04/15/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/best-courses-resources-feb-23">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/02/Python-programming-language-Feature_1290x688_MS1-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Writing & Content
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Best Courses &#038; Resources from the Web &#8211; Week of Feb. 23, 2015
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/23/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;2 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/what-is-python">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/Python-programming-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    What Is Python?
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/02/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;3 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/blogs-about-python-will-help-build-coding-skills">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/blogs-about-Python-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Blogs About Python That Will Help You Build Coding Skills
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/05/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;3 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/free-stuff-cool-reads-around-web-week-december-1-2014">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/11/Free-And-Cool-Around-The-Web-Teal-Feature_1290x688_KL-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Healthcare & Life Sciences
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Free Stuff and Cool Reads from Around the Web – Week of December 1, 2014
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;12/01/2014div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

        </ul>
    </div>
</div>

<div class="bx-wrapper slider-3-slides">
    <div class="bx-slider-container">
        <div class="control-list  bx-controls-direction">
            <span id="bxslider-prev-articleTablet"></span>

                <span class="control-list-font">Our Trending Articles</span>

            <span id="bxslider-next-articleTablet"></span>
        </div>

            <a class="button" href="/articles?topic_ids=5">VIEW ALL</a>


        <ul class="bxslider" rel="articleTablet">

            <li class="large-3 columns">
                <a href="/articles/test-drive-college-statistics-major">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Test-Drive-A-College-Statistics-Major-Feature_1290x688_KL-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Test Drive a College Statistics Major
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;08/31/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;8 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/best-mongodb-courses-online-tapping-big-demand-big-data">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/mongoDB-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Best MongoDB Courses Online: Tapping the Big Demand for Big Data Skills
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;07/03/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/5-paid-courses-learning-r-programming">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/paid-R-Program-courses-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    5 Paid Courses for Learning R Programming
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/08/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/41-tech-conferences-developers-data-scientists-engineers">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/02/tech-conferences-­Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    41 Technology Conferences for Developers, Data Scientists, and Engineers
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/03/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learn-google-analytics-with-these-courses">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Google-analytics-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Personal Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learn Google Analytics the Easy Way with these Courses
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;11/12/2012</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learning-sql-is-easy">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/SQL-database-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learning SQL Is An Easy Path to a $92k/Year Career
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/14/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;5 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/python-experts-to-follow">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/Python-experts-websites-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Python Experts to Follow
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/06/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learn-sql-today-make-big-job-market-tomorrow">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/learn-SQL-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learn SQL Today, Make It Big in the Job Market Tomorrow!
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;04/15/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/best-courses-resources-feb-23">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/02/Python-programming-language-Feature_1290x688_MS1-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Writing & Content
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Best Courses &#038; Resources from the Web &#8211; Week of Feb. 23, 2015
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/23/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;2 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

        </ul>
    </div>
</div>
<div class="bx-wrapper slider-2-slides">
    <div class="bx-slider-container">
        <div class="control-list  bx-controls-direction">
            <span id="bxslider-prev-articleTabletPortrait"></span>

                <span class="control-list-font">Our Trending Articles</span>

            <span id="bxslider-next-articleTabletPortrait"></span>
        </div>

            <a class="button" href="/articles?topic_ids=5">VIEW ALL</a>


        <ul class="bxslider" rel="articleTabletPortrait">

            <li class="large-3 columns">
                <a href="/articles/test-drive-college-statistics-major">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Test-Drive-A-College-Statistics-Major-Feature_1290x688_KL-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Test Drive a College Statistics Major
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;08/31/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;8 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/best-mongodb-courses-online-tapping-big-demand-big-data">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/mongoDB-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Best MongoDB Courses Online: Tapping the Big Demand for Big Data Skills
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;07/03/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/5-paid-courses-learning-r-programming">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/paid-R-Program-courses-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    5 Paid Courses for Learning R Programming
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/08/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/41-tech-conferences-developers-data-scientists-engineers">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/02/tech-conferences-­Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Software Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    41 Technology Conferences for Developers, Data Scientists, and Engineers
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;02/03/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learn-google-analytics-with-these-courses">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Google-analytics-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Personal Development
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learn Google Analytics the Easy Way with these Courses
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;11/12/2012</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/learning-sql-is-easy">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/SQL-database-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Learning SQL Is An Easy Path to a $92k/Year Career
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/14/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;5 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

        </ul>
    </div>
</div>

<div class="bx-wrapper show-for-small-only">
    <div class="bx-slider-container">
        <div class="control-list  bx-controls-direction">
            <span id="bxslider-prev-articleMobile"></span>

                <span class="control-list-font">Our Trending Articles</span>

            <span id="bxslider-next-articleMobile"></span>
        </div>

           <a class="button" href="/articles?topic_ids=5">VIEW ALL</a>


        <ul class="bxslider" rel="articleMobile">

            <li class="large-3 columns">
                <a href="/articles/test-drive-college-statistics-major">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Test-Drive-A-College-Statistics-Major-Feature_1290x688_KL-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Test Drive a College Statistics Major
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;08/31/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;8 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/best-mongodb-courses-online-tapping-big-demand-big-data">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/mongoDB-logo-website-Feature_1290x688_MS-600x400.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    Best MongoDB Courses Online: Tapping the Big Demand for Big Data Skills
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;07/03/2014</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;7 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

            <li class="large-3 columns">
                <a href="/articles/5-paid-courses-learning-r-programming">
    <div class="article-tile">
        <div class="article-tile-image">
            <img width="300" height="160" onerror="$(this).attr('src','http://cdn.skilledup.com/public/images/Articel-Default-Image.png')" src="http://cdn.skilledup.com/wp-content/uploads/2015/01/paid-R-Program-courses-Feature_1290x688_MS-600x320.jpg" alt="article image">
        </div>
        <div class="article-tile-main">
            <h2 class="tile-header-topic topic-2-color">
                Data Science
            </h2>
            <div class="tile-header-top-border">
                <div class="tile-title-top-border-left"></div>
                <div class="tile-title-top-border-right"></div>
            </div>
            <div class="article-subject-container">
                <h3 class="tile-subject">
                    5 Paid Courses for Learning R Programming
                </h3>
            </div>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
        </div>

        <div class="item-details">
            <div class="item-details-container">
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Calendar-Icon-Dark-Gray"></span>&nbsp;01/08/2015</div>
                </div>
                <div class="table-cell">
                    <div class="details-text"><span class="Sprite-Duration-Icon-Dark-Gray"></span>&nbsp;4 minutes</div>
                </div>
            </div>
        </div>
    </div>
</a>
            </li>

        </ul>
    </div>
</div>
    </div>

    <div class="row">
        <div class="bx-wrapper slider-top-careers show-for-large-up">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-career"></span>

                        <span class="control-list-font">Related Careers</span>

                    <span id="bxslider-next-career"></span>


                </div>
                <a class="button" href="/careers?topic_ids=5">VIEW ALL CAREERS</a>
                <ul class="bxslider" rel="career">



                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/statistician">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Statistician
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $59-$110K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/data-engineer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Engineer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $84-$155K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            NOT AVAILABLE
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/database-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $63-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            0%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/bi-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            BI Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $66-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/computer-scientist">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Computer Scientist
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $58-$128K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            20%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/data-architect">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Architect
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $89-$152K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/oracle-dba">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Oracle DBA
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $53-$100K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -20%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/sql-dba">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            SQL DBA
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $53-$100K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -15%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/database-analyst">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Analyst
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $59-$97K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            0%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/bi-analyst">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            BI Analyst
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $60-$106K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/bi-architect">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            BI Architect
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $90-$150K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -10%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/database-administrator-dba">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Administrator (DBA)
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $53-$100K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -15%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/sql-server-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            SQL Server Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $63-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -20%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/statistical-analyst">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Statistical Analyst
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $40-$90K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/bi-manager">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            BI Manager
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $84-$126K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/data-analyst">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Analyst
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $40-$84K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            25%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>





                            <li class="columns">
                                <div style="margin-top: 10px; margin-bottom: 10px;">
                                    <a href="/careers/database-architect">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Architect
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $89-$152K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                                </div>



                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <a href="/careers/data-warehouse-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Warehouse Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $61-$123K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                            </div>
                            </li>



                </ul>
            </div>
        </div>

        <div class="bx-wrapper slider-top-careers slider-3-slides">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-careerTablet"></span>

                        <span class="control-list-font">Related Careers</span>

                    <span id="bxslider-next-careerTablet"></span>


                </div>
                <a class="button" href="/careers?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="careerTablet">

                        <li class="large-3 columns">
                            <a href="/careers/statistician">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Statistician
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $59-$110K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/data-engineer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Engineer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $84-$155K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            NOT AVAILABLE
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/database-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $63-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            0%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/bi-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            BI Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $66-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/computer-scientist">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Computer Scientist
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $58-$128K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            20%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/data-architect">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Architect
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $89-$152K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/oracle-dba">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Oracle DBA
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $53-$100K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -20%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/sql-dba">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            SQL DBA
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $53-$100K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -15%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/database-analyst">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Analyst
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $59-$97K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            0%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                </ul>
            </div>
        </div>
        <div class="bx-wrapper slider-top-careers slider-2-slides">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-careerTabletPortrait"></span>

                        <span class="control-list-font">Related Careers</span>

                    <span id="bxslider-next-careerTabletPortrait"></span>


                </div>
                <a class="button" href="/careers?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="careerTabletPortrait">

                        <li class="large-3 columns">
                            <a href="/careers/statistician">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Statistician
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $59-$110K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/data-engineer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Engineer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $84-$155K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            NOT AVAILABLE
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/database-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $63-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            0%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/bi-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            BI Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $66-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/computer-scientist">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Computer Scientist
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $58-$128K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            20%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/data-architect">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Architect
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $89-$152K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                </ul>
            </div>
        </div>

        <div class="bx-wrapper slider-top-careers show-for-small-only">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-careerMobile"></span>

                        <span class="control-list-font">Related Careers</span>

                    <span id="bxslider-next-careerMobile"></span>


                </div>
                <a class="button" href="/careers?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="careerMobile">

                        <li class="large-3 columns">
                            <a href="/careers/statistician">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Statistician
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $59-$110K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            -5%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/data-engineer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Data Engineer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $84-$155K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            NOT AVAILABLE
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                        <li class="large-3 columns">
                            <a href="/careers/database-developer">
<div class="career-tile">
    <div class="career-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h2 class="tile-header-subject">
            Database Developer
            </h2>
            <div class="tile-header-bottom-border">
                <div class="tile-title-bottom-border-left"></div>
                <div class="tile-title-bottom-border-right"></div>
            </div>
    </div>
    <div class="career-tile-side-info">
        <div class="career-tile-side-top">
            <h3 class="career-tile-side-header-topic">
                avg salary
            </h3>
          <span class="career-tile-side-data">
              $63-$114K
          </span>
        </div>
        <div class="career-tile-side-bottom">
            <!--
            <h3 class="career-tile-side-header-topic">
                annual growth
            </h3>
          <span class="career-tile-side-data">
            0%
          </span>
          -->
        </div>
    </div>
</div>
</a>
                        </li>

                </ul>
            </div>
        </div>
    </div>



    <div class="row">
        <div class="bx-wrapper slider-top-skills show-for-large-up">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-skill"></span>

                        <span class="control-list-font">Top Skills</span>

                    <span id="bxslider-next-skill"></span>

                </div>
                <a class="button" href="/skills?topic_ids=5">VIEW ALL TOP SKILLS</a>
                <ul class="bxslider" rel="skill">

                    <li class="large-3 columns">
                        <a href="/skills/analytics">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            analytics
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">138</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/databases">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            databases
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">109</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/no-sql">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            no sql
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">66</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/sql-server">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            sql server
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">31</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/r">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            r
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">25</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-analysis">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data analysis
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">23</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-science">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data science
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">22</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-model">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data model
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">20</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-warehouses">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data warehouses
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">15</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/etl">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            etl
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">15</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/relational-database">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            relational database
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">14</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/database-design">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            database design
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">14</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/performance-tuning">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            performance tuning
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">14</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-centers">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data centers
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">13</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/indexing">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            indexing
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">13</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-management">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data management
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">12</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/stored-procedures">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            stored procedures
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">12</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/sas">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            sas
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">12</span>
    </div>
</div>
</a>
                    </li>

                </ul>
            </div>
        </div>

        <div class="bx-wrapper slider-top-skills slider-3-slides">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-skillTablet"></span>

                        <span class="control-list-font">Top Skills</span>

                    <span id="bxslider-next-skillTablet"></span>

                </div>
                <a class="button" href="/skills?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="skillTablet">

                    <li class="large-3 columns">
                        <a href="/skills/analytics">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            analytics
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">138</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/databases">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            databases
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">109</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/no-sql">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            no sql
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">66</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/sql-server">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            sql server
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">31</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/r">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            r
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">25</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-analysis">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data analysis
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">23</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-science">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data science
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">22</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-model">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data model
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">20</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-warehouses">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data warehouses
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">15</span>
    </div>
</div>
</a>
                    </li>

                </ul>
            </div>
        </div>

        <div class="bx-wrapper slider-top-skills slider-2-slides">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-skillTabletPortrait"></span>

                        <span class="control-list-font">Top Skills</span>

                    <span id="bxslider-next-skillTabletPortrait"></span>

                </div>
                <a class="button" href="/skills?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="skillTabletPortrait">

                    <li class="large-3 columns">
                        <a href="/skills/analytics">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            analytics
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">138</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/databases">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            databases
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">109</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/no-sql">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            no sql
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">66</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/sql-server">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            sql server
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">31</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/r">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            r
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">25</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/data-analysis">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            data analysis
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">23</span>
    </div>
</div>
</a>
                    </li>

                </ul>
            </div>
        </div>

        <div class="bx-wrapper slider-top-skills show-for-small-only">
            <div class="bx-slider-container">
                <div class="control-list  bx-controls-direction">
                    <span id="bxslider-prev-skillMobile"></span>

                        <span class="control-list-font">Top Skills</span>

                    <span id="bxslider-next-skillMobile"></span>

                </div>
                <a class="button" href="/skills?topic_ids=5">VIEW ALL</a>

                <ul class="bxslider" rel="skillMobile">

                    <li class="large-3 columns">
                        <a href="/skills/analytics">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            analytics
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">138</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/databases">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            databases
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">109</span>
    </div>
</div>
</a>
                    </li>

                    <li class="large-3 columns">
                        <a href="/skills/no-sql">
<div class="skill-tile">
    <div class="skill-tile-main">
        <div class="tile-header-topic topic-2-color">
            Data Science
        </div>
        <div class="tile-header-top-border">
            <div class="tile-title-top-border-left"></div>
            <div class="tile-title-top-border-right"></div>
        </div>
        <h3 class="tile-header-subject">
            no sql
        </h3>
        <div class="tile-header-bottom-border">
            <div class="tile-title-bottom-border-left"></div>
            <div class="tile-title-bottom-border-right"></div>
        </div>
    </div>

    <div class="tile-footer">
        <h4>careers need this skill</h4>
        <span class="career-skills-num">66</span>
    </div>
</div>
</a>
                    </li>

                </ul>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="large-12 columns">

<div class="container form-input newsletter">
    <div class="waiting">
        <table>
            <tr>
                <td>
                    <img width="64" height="64" src="http://cdn.skilledup.com/public/images/bx_loader_big.gif">
                </td>
            </tr>
        </table>
    </div>

    <input type="hidden" name="list" value="products" />
    <div class="title-updates"> Newsletter Signup </div>
    <div class="row">
        <div class="columns large-4 medium-4 small-12">
            <input type="text" name="fname" placeholder="Full Name" />
        </div>
        <div class="columns large-5 medium-5 small-12">
            <input type="email" name="email" placeholder="Email Address" />
        </div>
        <div class="columns large-3 medium-3 small-12">
            <div class="updates-button" onclick="handleEmailSubscription($(this).closest('.form-input'))">GET UPDATES</div>
        </div>
    </div>
    <div class="error-message"></div>
</div>
        </div>
    </div>
</div>

<link href='http://fonts.googleapis.com/css?family=Roboto:400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Roboto+Condensed:400,700' rel='stylesheet' type='text/css'>

<style type="text/css">
#MC_News_modal {text-align:center; margin: 0 auto; border-radius:4px; -moz-border-radius:4px; -webkit-border-radius:4px;overflow: auto;}
#close_popup{float:right; padding-right: 10px;  padding-top: 10px; height: 30px;}
.title_brackets{display:block; margin-right: auto; margin-left: auto; margin-top: 20px; width: 90px;}
#MC_News_modal h5 {padding-top:30px; font-family: 'Roboto Bold', sans-serif;font-size: 14px; color:  #333333; font-weight: bold;}
#MC_News_modal h2 {padding-top:20px; font-family: 'Roboto Condensed', sans-serif;font-size: 50px; color: #333333;font-weight: bold; line-height: 60px;}
#MC_News_modal p { text-align:center; font-family: 'Roboto Medium', sans-serif; font-size: 20px; color: #999999; line-height: 26px; font-weight: medium;  padding-top: 30px;}
#MC_News_modal footer {background-color: #00a1e1; border:none; border-top: 1px solid #e7e7e7; border-radius: 4px; -moz-border-radius:4px; -webkit-border-radius:4px; margin-top: 20px; width: 100%;height: 30%; overflow: auto; }
#footer_content { width: 90%; display: block; margin-left: auto;  margin-right: auto;}
.MC_modal_button, .MC_modal_button:hover{ background-color: #e9b64d; font-family: 'Roboto Bold', sans-serif; font-size: 14px; color: white; display: block; font-size: 0.875rem; margin: 0 0 1rem 0; padding: 0.8rem; height: 3.2rem; width: 100%; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; transition: box-shadow 0.45s, border-color 0.45s ease-in-out;}
.MC_modal_subtext{ font-family: 'Roboto Medium', sans-serif; font-size: 14px; color: white; text-align: center; float: left;}
.MC_modal_subtext_right{font-family: 'Roboto Medium', sans-serif; font-size: 14px; color: white; text-decoration: underline; text-align: center; float: right; }
#newsletter_container { overflow: auto; }
</style>

<div style="display: none; width:100%; height:100%; position:fixed; background:#000000; opacity: .7; filter:alpha(opacity=0.8); z-index:999998; top: 0; left: 0;" class="newsletter_popup_bg " id="exitpopup_bg "></div>


<aside style="width:63%; max-height:700px; margin:0px auto; display:none; position:fixed; color:black;  z-index:999999; background:#F8F8F8;" class="newsletter_popup " id="MC_News_modal">
	<div  id="newsletter_container" >
			<a><img  class="close_icon" style="" id="close_popup"
			src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Close-Icon-Small-DarkGray.png" alt="placeholder"></a>

		<div style="width: 70%; display: block; margin-left: auto;  margin-right: auto; overflow: auto; ">
			<h5 style="font-family: font-size: 15px;" >STAY UP TO DATE!</h5>
			<img class="title_brackets" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Title-Bracket-Top-DarkGray-2x.png">
			<h2>There are a lot of great courses out there. We find the best.</h2>
			<img  class="title_brackets" src="http://cdn.skilledup.com/wp-content/uploads/2014/10/Title-Bracket-Bottom-DarkGray-2x.png">
			<div style="width: 95%; display: block; margin-left: auto;  margin-right: auto;">
				<p style="line-height: 30px;">Whether it's low-cost or free courses, e-books, interviews with experts, or how-to-guides, we want to help you find the best stuff that's going to save you time and help you learn. Get our once-a-week newsletter for the latest and greatest online courses!</p>
			</div>
		</div>
		<footer>
	 		<div id="mc_embed_signup" >
	 			<form>
	 					<div class="row">
	 						<div id="footer_content">
	 							 <div class="form">
                    <input type="hidden" name="list" value="master">
                  <div class="columns large-4">
                    <input style=" height: 70px; background-color: white; color: #999999;font-size: 14px;"  class="full-width" placeholder="Full Name" name="fname" />
                  </div>
                  <div class="columns large-4" >
                    <input  style=" height: 70px; background-color: white; color: #999999;font-size: 14px;" class="full-width" placeholder="Email Address" name="email" />
                  </div>
                  <div class="columns large-4" >
                    <span class="button MC_modal_button" style="height: 70px; padding-top: 30px;" onclick="handleEmailSubscription($(this).closest('.form'))">GET UPDATES</span>
                  </div>
                    <div style="color: red;" class="error-message"></div>
                </div>

					        <div style="width: 100%; display: block; margin-left: auto;  margin-right: auto; " >
					        <div class="columns large-8" >
						      	<div  class="MC_modal_subtext">
						        </div>
						      </div>
						      <div class="columns large-4" >
			          		<a  class="MC_modal_subtext_right close_icon" >
			          			No thanks, I am too skilled as it is!
			          		</a>
			          	</div>
			          </div>
	 						</div>
	 					</div>
	 			</form>
	 		</div>
	 		</footer>
	 	<div>
	</aside>

    <div id="root-container-footer"></div>
</div>

<div class="modal-layer fixed gray-xlight waiting">
    <table style="height: 100%; width:100%;">
        <tr><td style="height: 100%; width: 100%; vertical-align: center; text-align: center;">
            <img style="width: 64px; height: 64px;" width="64" height="64" src="http://cdn.skilledup.com/public/images/bx_loader_big.gif">
        </td></tr>
    </table>
</div>




<div id="logged-in"></div>

  <script type="text/javascript">
      root_url = "/";
      root_api_url = "/api/v3/";
      base_static_path = "http://cdn.skilledup.com/";
  </script>




    <script type="text/javascript" src="/static/public/js/common.js?a587c4a2"></script>






<footer>
    <div class="row">
        <div class="column large-3 medium-3 small-6">
            <h4>About</h4>
            <ul class="no-bullet">
                <li><a href="/about/">Our Story</a></li>
                <li><a href="/about/#about-team">Join Our Team</a></li>
                <li><a href="/about/#about-contact">Contact Us</a></li>
                <li><a href="/podcast">Fearless Careers Podcast</a></li>
<!--  Temporary disabled MV Feb 2nd 2015             <li><a href="/new-partner">New Partner Form</a></li> -->
<!--                <li><a href="/partner-profile">Partner Profile</a></li> -->
            </ul>
        </div>
        <div class="column dots large-3 medium-3 small-6">
            <h4>Resources</h4>
            <ul class="no-bullet">
                <li>
                    <a href="http://skilledup.zendesk.com/" target="_blank" title="Help Center">
                        Help Center
                    </a>
                </li>
                <li><a href="/terms-of-use/">Terms of Use</a></li>
                <li><a href="/privacy-policy/">Privacy Policy</a></li>
            </ul>
        </div>
        <div class="column large-6 medium-6 small-12 big">
            <div class="footer-trends-container">
              <h4>Business Trends &amp; Insights</h4>
              <ul class="no-bullet" id="latest-blog-list">


                    <li><a href="/insights/net-neutrality-debate-mean-edtech">The Net Neutrality Debate: What Does It Mean For Edtech?</a></li>
                    <hr>

                    <li><a href="/insights/tackle-data-scientist-skills-gap-company">How To Tackle The Data Scientist Skills Gap For Your Company</a></li>



              </ul>
            </div>
        </div>
    </div>
    <div class="row social">
        <div class="large-12 medium-12 text-center footer-snippet">
            <h4>Follow.&nbsp;&nbsp; Learn.&nbsp;&nbsp; Grow.</h4>
        </div>
        <div class="column large-3 medium-6 small-6">
            <a href="https://www.linkedin.com/company/skilledup" target="_blank"><div class="Sprite-social_linkedin social-button linkedin"></div></a>
        </div>
        <div class="column large-3 medium-6 small-6">
            <a href="https://www.facebook.com/skilledup" target="_blank"><div class="Sprite-social_facebok social-button facebook"></div></a>
        </div>
        <div class="column large-3 medium-6 small-6">
            <a href="https://plus.google.com/+Skilledup/" target="_blank"><div class="Sprite-social_google social-button google"></div></a>
        </div>
        <div class="column large-3 medium-6 small-6">
            <a href="https://twitter.com/skilledup" target="_blank"><div class="Sprite-social_twitter social-button twitter"></div></a>
        </div>
    </div>
    <div class="row"><div class="column large-12 medium-12 small-12">
        <div class="copyright"><span class="year">&copy; </span> Apollo Lightspeed, LLC. All rights reserved.</div>
    </div></div>
</footer>

</body>
</html>
'''


def split_content_and_replace_links():
    content_to_replace, content_as_is = (file_content[:len(file_content)/2], file_content[len(file_content)/2:])
    replace_url = '\"http://www.google.com\"'

    # Look for anything that is http, https or www
    regex_pattern = '(([\'\"]http[s]?://)|([\'\"]//www.))(.*?)([\"\'])'
    replaced_content = re.sub(regex_pattern, replace_url, content_to_replace)

    # Look for anything that starts with href
    regex_pattern = '(href=")(.*?)([\"\'])'
    replaced_content = re.sub(regex_pattern, 'href=' + replace_url, replaced_content)

    # Look for anything that starts with src
    regex_pattern = '(src=")(.*?)([\"\'])'
    replaced_content = re.sub(regex_pattern, 'src=' + replace_url, replaced_content)

    final_content = replaced_content + content_as_is
    print final_content
    return final_content

split_content_and_replace_links()
