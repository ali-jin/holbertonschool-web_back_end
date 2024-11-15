export default function updateStudentGradeByCity(arrayStudent, city, newGrades) {
  return arrayStudent
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.find(
        (grade) => grade.studentId === student.id
      );
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
