<?php

require_once('PHPMail/class.phpmailer.php');

if ($_SERVER["REQUEST_METHOD"] == "POST")
{   

if (empty($_POST["name"]))
    {$nameErr = "Name is required";}
  else
    {$name = test_input($_POST["name"]);}
    
if (empty($_POST["email"]))
    {$emailErr = "email address is required";}
  else
    {$email_to = test_input($_POST['email']);}
    
if (empty($_POST["message"]))
    {$messageErr = "No map has been included";}
  else
    {$message = test_input($_POST['message']);}    

  $from ='gis@mesacounty.us';
}

function test_input($data)
{
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

$mail = new PHPMailer(true);

$mail->IsSMTP();
$mail->SMTPAuth = false;
$mail->Host = "smtprelay.internal.mesacounty.us";
$mail->Port = 25;

$mail->SetFrom($from,'Mesa County GIS');
$mail->Subject = $name." Has Shared a Map View With You";
$mail->MsgHTML($message);
$mail->AddAddress($email_to);

if(!$mail->Send()) {
	echo "Mailer Error: " . $name->ErrorInfo;
} else {
  echo "Message sent!";
}
?>
