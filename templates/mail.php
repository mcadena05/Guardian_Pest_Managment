<?php
//get data from form  

$name = $_POST['name'];
$phone= $_POST['phone'];
$message= $_POST['message'];
$city= $_POST['city'];
$state= $_POST['state'];
$zip= $_POST['zip'];
$to = "cadenamarlynn@gmail.com";
$subject = "Quote request from Website";
$txt ="Name = ". $name . "\r\n  Email = " . $email . "\r\n Message =" . $message ." \r\n Location = " . $city $state $zip;
$headers = "From: noreply@yoursite.com" . "\r\n" .
"CC: somebodyelse@example.com";
if($email!=NULL){
    mail($to,$subject,$txt,$headers);
}
//redirect
header("homepage.html");
?>