export default function getListStudentIds(arrayObj) {
  let arrayId = [];
  if (Array.isArray(arrayObj)) {
    arrayId = arrayObj.map((student) => student.id);
  }
  return arrayId;
}
