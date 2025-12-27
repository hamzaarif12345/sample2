async function mergePDFs() {
  const input = document.getElementById("pdfFiles")
  const files = input.files

  if (!files.length) {
    alert("Please select at least one PDF file.")
    return
  }

  const { PDFDocument } = PDFLib
  const mergedPdf = await PDFDocument.create()

  for (const file of files) {
    const arrayBuffer = await file.arrayBuffer()
    const pdf = await PDFDocument.load(arrayBuffer)

    const copiedPages = await mergedPdf.copyPages(
      pdf,
      pdf.getPageIndices()
    )

    copiedPages.forEach(page => mergedPdf.addPage(page))
  }

  const mergedPdfBytes = await mergedPdf.save()

  // Create download link
  const blob = new Blob([mergedPdfBytes], { type: "application/pdf" })
  const url = URL.createObjectURL(blob)

  const a = document.createElement("a")
  a.href = url
  a.download = "merged.pdf"
  document.body.appendChild(a)
  a.click()

  URL.revokeObjectURL(url)
  a.remove()
}
