export default function getListStudentIds(arrayObj) {
  let arrayId = [];
  if (Array.isArray(arrayObj)) {
    arrayId = [arrayObj[0].id, arrayObj[1].id, arrayObj[2].id]
  }
  return arrayId;
}
