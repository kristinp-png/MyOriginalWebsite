<!-- Kristin Pondexter | May 25, 2025 | Figma to HTML Assignment -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Feedback Form - ClickSavvy</title>
</head>
<body>
  <header>
    <h1>ClickSavvy</h1>
    <nav>
      <p>
        <a href="home.html">Home</a> |
        <a href="cyberthreats.html">Cyber Threats 101</a> |
        <a href="protect.html">Protect Yourself 102</a>
      </p>
    </nav>
  </header>

  <section>
    <h2>We’d Love Your Feedback</h2>
    <p>Let us know how we can make <em>ClickSavvy</em> even better.!</p>
    <p>Contact us if you have any questions</p>

    <form action="#" method="post">
      <label for="email">Email Address:</label><br>
      <input type="email" id="email" name="email" placeholder="example@email.com"><br><br>

      <label>Your overall satisfaction:</label><br>
      <input type="radio" name="rating" value="1"> ★
      <input type="radio" name="rating" value="2"> ★★
      <input type="radio" name="rating" value="3"> ★★★
      <input type="radio" name="rating" value="4"> ★★★★
      <input type="radio" name="rating" value="5"> ★★★★★<br><br>

      <label for="feedback">Please leave your feedback below:</label><br>
      <textarea id="feedback" name="feedback" rows="5" cols="40" placeholder="Type here..."></textarea><br><br>

      <button type="submit">Submit</button>
    </form>
  </section>

  <footer>
    <p>Contact Info: 803.662.4989 | info@clicksavvy.com</p>
  </footer>
</body>
</html>
