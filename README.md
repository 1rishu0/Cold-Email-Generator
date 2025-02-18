# Cold-Email-Generator

Create personalized cold emails effortlessly with our Cold Email Generator powered by Llama 3.3, LangChain, and LLMs. Generate engaging, AI-driven emails tailored to your audience, boosting conversions and outreach efficiency. Perfect for sales, marketing, and networking!

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Dynamic Email Generation:** Input a company's career page URL and generate cold emails tailored with required skills.
- **AI-Driven Personalization:** Leverages LLMs to create engaging, context-specific emails.
- **Seamless Integration:** Utilizes LangChain for efficient prompt management and workflow.
- **Vector Embedding:** Uses ChromaDB for robust vector embedding to enhance search and context extraction.
- **User-Friendly Interface:** Built with Streamlit for an intuitive and interactive user experience.

---

## Technologies Used

- **Python:** Core programming language for the application.
- **Groq Cloud:** Cloud infrastructure for scalable operations.
- **LangChain:** Manages LLM prompt chains and interactions.
- **Streamlit:** Provides the front-end interface.
- **ChromaDB:** Handles vector embeddings for skill extraction.
- **Llama3.3:** The LLM powering the email generation.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/cold-email-generator.git
   cd cold-email-generator
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration:**

   - Set up your Groq Cloud credentials and any other API keys required in the `.env` file.
   - Ensure proper configuration of LangChain and ChromaDB as per their documentation.

---

## Usage

1. **Run the Application:**

   ```bash
   streamlit run .\app\main.py
   ```

2. **Input Required Information:**

   - Enter the URL of the company's careers page.
   - Specify the required skills for the job.

3. **Generate Email:**

   - Click the 'Generate Email' button to see the AI-crafted cold email tailored to the input data.

---

## Demo

**Video Demonstration:**

[*Insert your video demonstration here (e.g., embed a YouTube video or include a link to the video)*](https://github.com/user-attachments/assets/9a614303-6a95-4114-a415-61671aafc6d1)

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

---

## License

Distributed under the GPL-3.0 License. 

