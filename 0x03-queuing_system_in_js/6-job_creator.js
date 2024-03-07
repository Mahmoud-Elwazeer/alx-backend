const kue = require('kue');

const queue = kue.createQueue();

const details = {
  phoneNumber: 'phoneNumber',
  message: 'message',
};

const job = queue.create('push_notification_code', details);

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
})
