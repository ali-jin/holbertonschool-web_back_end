import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(), uploadPhoto()])
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
