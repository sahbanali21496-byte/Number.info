export default async function handler(req, res) {
  try {
    const num = req.query.num;

    // Number validation
    if (!num) {
      return res.status(400).json({
        error: "num parameter missing"
      });
    }

    if (!/^[0-9]{10}$/.test(num)) {
      return res.status(400).json({
        error: "invalid number format"
      });
    }

    const apiUrl = `https://abbas-apis.vercel.app/api/phone?number={num}`;

    const response = await fetch(apiUrl, {
      headers: {
        "User-Agent": "Number-Info-Web"
      }
    });

    if (!response.ok) {
      return res.status(502).json({
        error: "failed to fetch data"
      });
    }

    const data = await response.json();

    // 🔥 ONLY API DATA (NO EXTRA TEXT)
    res.setHeader("Content-Type", "application/json");
    res.status(200).json(data);

  } catch (err) {
    res.status(500).json({
      error: "server error"
    });
  }
}