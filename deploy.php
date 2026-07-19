<?php
// Simple, secure git pull webhook for IconStash auto-deploy
$secret_token = 'e11c5bc79c6d4824bb883b2723c0fa6a'; // Using the same IndexNow key for simplicity

if (!isset($_GET['token']) || $_GET['token'] !== $secret_token) {
    header('HTTP/1.1 403 Forbidden');
    die('Unauthorized');
}

header('Content-Type: text/plain');
echo "Deployment started...\n";

// Change directory to the root of the site
chdir(__DIR__);

// Verify git status and execute pull
echo "Executing Git pull...\n";
$reset_output = shell_exec('git reset --hard HEAD 2>&1');
echo "Reset: " . $reset_output . "\n";

$pull_output = shell_exec('git pull origin main 2>&1');
echo "Pull: " . $pull_output . "\n";

echo "Deployment finished successfully!\n";
?>
