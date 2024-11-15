export default function getStudentIdsSum(arrayStudent) {
  return arrayStudent.reduce((acc, student) => acc + student.id, 0);
}
