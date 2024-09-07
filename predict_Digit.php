<DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="4; url='draw_Page.html'" />
</head>
<body>
<?php
$check_Run = shell_exec("pgrep -f Digit_Network_Back.py");

if(strlen($check_Run) < 6){
echo "Neural network is currently down, ask Case to put it back up";
die;
}
else{
$hostname = "localhost";
$username = "digit_Site";
$password = "password";
$db = "digit_Recognizer";
$dbconnect = mysqli_connect($hostname,$username, $password, $db);

if($dbconnect ->connect_error){
die("Database connection failed: " . $dbconnect->connect_error);
}

if(isset($_POST['submit'])) {
  $vals=$_POST['details'];
  $actual = $_POST['actual'];
}
$out = shell_exec("cd /home/pi/Desktop/tensorFlow; . env/bin/activate; cd digit_Neural_Network; python back_Network/input_Test.py ".$vals."; deactivate");       
$query = mysqli_query($dbconnect, "INSERT INTO train_Data (input,output,value) values('$vals','$out','$actual');")
        or die(mysqli_error($dbconnect));
echo "The network predicts you drew a ".$out;
}
?>
</body>
</html>
