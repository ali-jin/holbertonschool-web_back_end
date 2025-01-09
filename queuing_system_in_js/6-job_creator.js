import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: "1567926782",
  message: "Your account has been created",
}

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
})

job.on('complete', function () {
  console.log('Notification job completed');

}).on('failed', function (err, done) {
  console.log('Notification job completed');
})
