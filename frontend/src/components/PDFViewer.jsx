import React, { useEffect, useRef, useState } from "react";
import * as pdfjsLib from "pdfjs-dist";
import pdfjsWorker from "pdfjs-dist/build/pdf.worker.entry"; // Import worker

pdfjsLib.GlobalWorkerOptions.workerSrc = pdfjsWorker; // Set the worker

const PDFViewer = ({ pdfUrl }) => {
	const canvasRef = useRef(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	useEffect(() => {
		const renderPDF = async () => {
			setLoading(true);
			try {
				const pdf = await pdfjsLib.getDocument(pdfUrl).promise;
				const page = await pdf.getPage(1); // Renders the first page of the PDF

				const viewport = page.getViewport({ scale: 1.5 });
				const canvas = canvasRef.current;
				const context = canvas.getContext("2d");

				canvas.height = viewport.height;
				canvas.width = viewport.width;

				const renderContext = {
					canvasContext: context,
					viewport: viewport,
				};

				await page.render(renderContext).promise;
				setLoading(false);
			} catch (err) {
				setError("Failed to load PDF");
				setLoading(false);
			}
		};

		if (pdfUrl) {
			renderPDF();
		}
	}, [pdfUrl]);

	return (
		<div>
			{loading && <p>Loading PDF...</p>}
			{error && <p>{error}</p>}
			<canvas ref={canvasRef} style={{ width: "100%" }} />
		</div>
	);
};

export default PDFViewer;
