# AccessAI Extension

AccessAI is a revolutionary Chrome extension designed to enhance web accessibility by automatically generating descriptive alt texts for images on any webpage. This extension is particularly useful for visually impaired users who rely on screen readers to navigate and understand content on the web.

## Key Features

- **Dynamic Alt Text Generation**: Automatically replaces missing or inadequate alt texts with detailed descriptions generated using advanced AI models.
- **Customizable Verbosity Levels**: Users can choose between low, medium, and high verbosity for descriptions to match their preference and context of use.
- **Accessibility Enhancement**: Increases the accessibility of web pages by ensuring that all images have meaningful descriptions, making content more accessible to visually impaired users.
- **Easy to Use**: Features a floating button on web pages that, when clicked, activates the alt text generation. This button can be easily moved across the screen for convenient access.
- **Privacy-Focused**: Does not store or transmit any personal data from the users' sessions.

## How It Works

The extension detects images on a webpage and sends the image URLs to a Flask backend server, where they are processed using a generative AI model to create descriptive alt texts. These texts are then sent back to the extension and automatically set as the images' new alt attributes.

## Installation

### Prerequisites

- Google Chrome Browser
- Internet access to connect with the backend service

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/accessai-extension.git
   cd accessai-extension
   ```

2. **Load the Extension into Chrome**
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable Developer Mode by clicking the toggle switch next to "Developer mode."
   - Click the "Load unpacked" button and select the directory containing your extension.

3. **Backend Setup**
   - Ensure you have Python 3.x installed on your system.
   - Navigate to the backend directory:
     ```bash
     cd backend
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Flask app:
     ```bash
     python main.py
     ```

## Usage

After installing the extension and running the backend server:
- Navigate to any webpage.
- Click the floating AccessAI button to activate the alt text generation.
- Choose the desired verbosity level from the extension's popup menu to generate the descriptions.

## Contributing

Contributions to the AccessAI extension are welcome! Please refer to the CONTRIBUTING.md file for guidelines on how to make contributions.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub issue tracker or contact the maintainers directly via email.