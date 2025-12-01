# Student Dropout Risk Predictor - Frontend
**Revised using Google Gemini 3**

The frontend for the Student Dropout Risk Predictor, built with [Nuxt 3](https://nuxt.com/). This application provides a user interface for inputting student data (either individually or in batch via CSV) to predict dropout risks.

## Features

- **Single Prediction:** Interactive form with client-side validation for individual student data entry.
- **Batch Prediction:** CSV file upload support for processing multiple student records at once.
- **Visualizations:** Results are displayed with risk scores and sorting capabilities.
- **Responsive Design:** Styled with SCSS for a clean, accessible interface.

## Prerequisites

- **Node.js:** v22 or higher
- **Package Manager:** `npm`, `pnpm`, or `yarn`

## Setup & Installation

1.  **Install Dependencies**:
    ```bash
    # npm
    npm install

    # pnpm
    pnpm install
    ```

2.  **Environment Configuration**:
    By default, the application expects the backend to be running at `http://127.0.0.1:5000/api`.
    To override this (e.g., for production), set the `API_URL` environment variable.

    You can create a `.env` file in the root of the `frontend` directory:
    ```bash
    API_URL=http://your-backend-url.com/api
    ```

## Development

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev
```

The application will be available at `http://localhost:3000`.

## Production Build

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build
```

Locally preview the production build:

```bash
npm run preview
```

## Project Structure

- `pages/`: Application routes (Home, About, etc.)
- `components/`: Reusable Vue components
- `assets/scss/`: Global styles and theme definitions
- `public/`: Static assets
- `nuxt.config.ts`: Nuxt configuration (API base URL, modules, etc.)
