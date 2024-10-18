import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      for (const value in values) {
        if (value === 'rejected') {
          value.value = `Error: ${value.reason.message}`;
          delete value.reason;
        }
      }
      return values;
    });
}
