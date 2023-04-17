<!DOCTYPE html>
<html>
<head>

</head>
<body>
<h1>RSA Geo Encryption</h1>
<p>This is a Python program that uses RSA encryption to encode and decode messages using geographic coordinates.</p>

<h2>Usage</h2>
<ol>
	<li>Install the required packages with <code>pip install -r requirements.txt</code></li>
	<li>Run the program with <code>python rsa_geo.py</code></li>
	<li>Enter a message to encrypt or decrypt, along with the latitude and longitude of the location to use for encryption/decryption</li>
</ol>

<h2>Example Output</h2>
<img src="example_output.png" alt="Example output of the RSA Geo Encryption program" width="800">

<h2>How it Works</h2>
<p>The program generates a public and private RSA key pair. When encrypting a message, the program uses the geographic coordinates to generate a random number to use as the encryption key. This key is then encrypted using the public RSA key and the resulting cipher is appended to the encrypted message. When decrypting a message, the program uses the geographic coordinates to generate the same random number and uses it to decrypt the cipher.</p>

<h2>Future Improvements</h2>
<ul>
	<li>Add support for using more than one set of geographic coordinates for encryption and decryption to increase security</li>
	<li>Implement a way to securely store the private RSA key so it does not need to be generated each time the program is run</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
